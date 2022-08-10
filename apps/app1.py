# Importing necessary library
import pandas as pd
import hydralit_components as hc
import time
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as components
import shap, joblib
from apps import app3 

# User input values (slider panel)
def user_input_features():   
    with st.sidebar.expander('Click here for inputs...', expanded=False): 
        Year = st.slider('Year', 2002, 2020, 2005)
        Month = st.selectbox("Month: ", ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September', 'October',
                                    'November', 'December'], 2)
        Replication = st.selectbox("Replication (Experimental zones)", ['R1', 'R2', 'R3', 'R4', 'R5'])
        N_rate = st.slider('N_rate (N fertilizer rate) [kg N ha-1]', 0, 220, 81)
        PP2 = st.slider('PP2 (Cumulative Precipitation in last two days before gas sampling) [mm]', float(0), float(100), 18.18)
        PP7 = st.slider('PP7 (Cumulative Precipitation in last week before gas sampling) [mm]', float(0), float(255), 38.11)
        Air_T = st.slider('Air_T (Daily average air temperature) [°C]', float(0), float(32), 23.93)
        DAF_TD = st.slider('DAF_TD (Days after top dressed N fertilizer) [Days]', 0, 700, 365)
        DAF_SD = st.slider('DAF_SD (Days after side dressed N fertilizer) [Days]', 0, 700, 50)
        WFPS25cm = st.slider('WFPS25cm (Water Filled Pore Space) [Fraction]', 0.02, 1.00, 0.43 )
        NH4 = st.slider('NH4 (Ammonium N content in the top 25-cm soil layer) [kg ha-1]', float(1), float(220), 8.78)
        NO3 = st.slider('NO3 (Nitrate N content in the top 25-cm soil layer) [kg ha-1]', float(1), float(220), 22.67)
        Clay = st.slider('Clay (Clay concentration in the top 25-cm soil layer) [g kg-1]', 50, 250, 150)
        SOM = st.slider('SOM (Soil Organic Matter concentration) [%]', float(1), float(5), 3.33)
        Data_Use = st.radio("Data_Use (Model phase: training/ testing)", ('Building', 'Testing'), 0)
        Vegetation = st.radio("Vegetation: ", ('Corn', 'GLYMX', 'TRIAE'), 0)
        
        st.sidebar.info('''
            **Note:** Is application run slow ? _Computation time (sec.) depends on your data complexity with server run._
        ''')
        st.sidebar.markdown('''<small>ML App with Explainable AI v2.0 | Sept 2022</small> Copyright &copy; Kunal K.''', unsafe_allow_html=True)

    # Order for displaying the features as dataframe
    data = {'Year': Year, 'Month': Month, 'Replication': Replication, 'Data_Use': Data_Use, 'N_rate': N_rate, 'PP2': PP2,
            'PP7': PP7, 'Air_T': Air_T, 'DAF_TD': DAF_TD, 'DAF_SD': DAF_SD, 'WFPS25cm': WFPS25cm, 'NH4': NH4, 'NO3': NO3,
            'Clay': Clay, 'SOM': SOM, 'Vegetation': Vegetation}
    features = pd.DataFrame(data, index=[0])

    return features

# Load model
@st.cache(allow_output_mutation=True)
def load_model():
    return joblib.load(open('model/model_xgb_61_final.joblib.compressed', 'r'))

# Explain model prediction results
def explain_model_prediction(data, model):
    explainer = shap.Explainer(model)
    shap_values = explainer(data)
    p = explainer.expected_value
    return p, shap_values

# Plot the force plot in streamlit in API
def st_shap(plot, height=None):
    shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
    components.html(shap_html, height=height)

def shap_summary_plot(df, model):
    p, shap_values = explain_model_prediction(df, model)
    st.subheader('i) Impact on model output')
    app3.text('It shows contributing the each features to push the model output from the base value. \
            Features pushing the prediction <b>higher</b> are shown in <b>red</b>, \
            those pushing the prediction <b>lower</b> are in <b>blue</b>.')

    fig1,ax1 = plt.subplots()
    ax1.set_title('Impact analysis')
    shap.plots.waterfall(shap_values[0], max_display=14)
    st.pyplot(fig1)
    
    st.subheader('ii) Visualize your record with prediction')
    st_shap(shap.force_plot(p, shap_values.values[0,:], df.iloc[0,:]))

    st.subheader('iii) Summary plot I')
    fig2,ax2 = plt.subplots()
    ax2.set_title('Feature Importance (Scatter)')  
    shap.summary_plot(shap_values, df)
    st.pyplot(fig2)

    st.subheader('iii) Summary plot II - Feature importances')
    fig3,ax3 = plt.subplots()
    ax3.set_title('Feature Importance (Bar)')
    shap.summary_plot(shap_values, df, plot_type='bar')
    st.pyplot(fig3)

def app():   
    model = load_model()

    st.sidebar.subheader('i) Specify user inputs data:')
    df = user_input_features()

    # Show selected inputs as dataframe
    app3.header('A) Selected inputs:')
    app3.text('Below are the <b>input parameters</b> to model which are selected by user.')
    st.dataframe(data = df)
    app3.line_solid()

    # Data-preprocessing (Features endoding)
    months_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
                    'September': 9, 'October': 10, 'November': 11, 'December': 12}
    Vegetation_dict = {"Corn": 1, "GLYMX": 2, "TRIAE": 3}
    datause_dict = {"Building": 1, "Testing": 0}
    replication_dict = {"R1": 1, "R2": 2, "R3": 3, "R4": 4, "R5": 5}
    df["Month"] = df["Month"].apply(lambda x: months_dict[x])
    df["Vegetation"] = df["Vegetation"].apply(lambda x: Vegetation_dict[x])
    df["Data_Use"] = df["Data_Use"].apply(lambda x: datause_dict[x])
    df["Replication"] = df["Replication"].apply(lambda x: replication_dict[x])
    
    # Model predictions(XgbRegressor)
    prediction = model.predict(df)
    app3.header('B) Prediction of N2O:')
    app3.text('Find the predicted value of N2O with user selected. <b>Press Predict button</b>.')

    if st.button("Predict"):
        with hc.HyLoader('Loading...',hc.Loaders.standard_loaders,index=[0]):
            time.sleep(5)
            
        st.subheader('i) Predicted value :')
        st.write(round(prediction[0],3))
        st.text('Predictions are computed on your inputs and ML model (Xgb).')
        app3.line_solid()
    
        app3.header('C) Explainable AI - Model prediction results:')
        shap_summary_plot(df, model)
