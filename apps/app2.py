# Importing necessary library
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as components
import shap
from sklearn.metrics import r2_score, mean_squared_error
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import pybase64, joblib
from apps import app3


analyzed_status, user_selected_data, sample_data = 0, '', ''
op_var, data_s, op_data, r2, mse, exp_ai,  = '', '', '', 0, 0, 0

# Csv user data
def upload_data():
    st.sidebar.subheader('1. Upload data and analyze it:')
    with st.sidebar.expander('Click here to upload data...', expanded=False): 
        uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
        st.markdown("""
            [Example CSV input file](kkk)
        """)
        return uploaded_file

# Sample dataset
def load_data():
    try:
        sample = pd.read_csv('data/sample_data.csv')
        return sample
    except:
        st.write('Unable to fetch sample dataset.')
        return None

# Load model
@st.cache(allow_output_mutation=True)
def load_model():
    try:
        return joblib.load(open('model/model_xgb_61_final.joblib.compressed', 'rb'))
    except:
        st.error('Unable to fetch model, please configure the model path...')
        return None
        
def download_link(object_to_download, download_filename, download_link_text):
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)
    b64 = pybase64.b64encode(object_to_download.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

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

def shap_summary_plot(df, model, i):
    p, shap_values = explain_model_prediction(df, model)
    st.subheader('i) Impact on model output')
    app3.text('It shows contributing the each features to push the model output from the base value. \
            Features pushing the prediction <b>higher</b> are shown in <b>red</b>, \
            those pushing the prediction <b>lower</b> are in <b>blue</b>.')

    fig1,ax1 = plt.subplots()
    ax1.set_title('Impact analysis')
    shap.plots.waterfall(shap_values[i], max_display=14)
    st.pyplot(fig1)
    
    st.subheader('ii) Visualize your record with prediction')
    st_shap(shap.force_plot(p, shap_values.values[i], df.iloc[i]))

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

# Model predictions
def build_model(model, data):
    try:
        dataset = data.copy()
        x = dataset.drop(columns=['N2O'])
        y = dataset['N2O']
        nm = y.name

        # Data-preprocessing
        dataset = dataset.dropna()
        
        months_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
                        'September': 9, 'October': 10, 'November': 11, 'December': 12}
        Vegetation_dict = {"Corn": 1, "GLYMX": 2, "TRIAE": 3}
        datause_dict = {"Building": 1, "Testing": 0}
        replication_dict = {"R1": 1, "R2": 2, "R3": 3, "R4": 4, "R5": 5}
        dataset["Month"] = dataset["Month"].apply(lambda x: months_dict[x])
        dataset["Vegetation"] = dataset["Vegetation"].apply(lambda x: Vegetation_dict[x])
        dataset["DataUse"] = dataset["DataUse"].apply(lambda x: datause_dict[x])
        dataset["Replication"] = dataset["Replication"].apply(lambda x: replication_dict[x])
        
        dataset = dataset[['Year', 'Month', 'DataUse', 'Replication', 'N_rate', 'PP2', 'PP7', 'AirT',	
                    'DAF_TD', 'DAF_SD', 'WFPS25cm', 'NH4', 'NO3', 'Clay', 'SOM', 'N2O', 'Vegetation']]
        data_shap = dataset.drop(['N2O'], axis=1)
        if 'N2O' in dataset.columns:
            prediction = model.predict(dataset.drop(['N2O'], axis=1))
            output_data = data.loc[dataset.index]             
            output_data['Prediction'] = pd.DataFrame(prediction)
            acc = r2_score(dataset.N2O, prediction).round(2)
            err = mean_squared_error(dataset.N2O, prediction).round(2)
            return nm, output_data, acc, err, data_shap
        else:
            st.error('Unsssable to proceed with model, Please configure the output variable (name/ column/ values)...')
    except:
        st.error('Unable to proceed with model, Please configure the output variable (name/ column/ values)...')

def app():
    global user_selected_data, sample_data, analyzed_status, op_var, op_data, r2, mse, exp_ai, data_s

    app3.header('A) Upload data / use sample data:')
    file = upload_data()
    model = load_model()
    
    if file is not None:
        user_selected_data = pd.read_csv(file)
        app3.text('Below <b>data</b> is successfully uploaded by user. Use data as per provided format.')
        st.write(user_selected_data.head())
        analyzed_status = 1
        app3.line_solid()

        app3.header('B) Analyze your data:')
        app3.text('Find the data summary with visualizations. <b>Press Analyze Data button</b>.')
        if st.button("Analyze Data"):
            pr = ProfileReport(user_selected_data, orange_mode= True,
                    title="Agriculture Data N2O Prediction",
                    dataset={
                        "description": "This profiling focused on detailed data analysis for agricultural sector",
                        "copyright_holder": "Kunal K",
                        "copyright_year": "2021",
                        "url": "https://www.linkedin.com/in/kunalkolhe3/",},
                )
            st_profile_report(pr)
    else:
        st.info('Please upload csv file from left-side panel.')
        if st.button('Press to use Sample dataset'):
            app3.text('Below data is <b>sample dataset</b>.')
            sample_data = load_data()
            if sample_data is not None:
                st.write(sample_data.head())
                analyzed_status = 2
                app3.line_solid()
                
                app3.header('B) Analyze sample data:')
                app3.text('Find the data summary with visualizations for sample data. <b>Press Analyze Data button</b>.')
                if not st.button("Analyze Data"):
                    print('aaaaa')
                    pr = ProfileReport(sample_data, orange_mode= True,
                        title="Agriculture Data N2O Prediction",
                        dataset={
                            "description": "This profiling focused on detailed data analysis for agricultural sector",
                            "copyright_holder": "Kunal K",
                            "copyright_year": "2021",
                            "url": "https://www.linkedin.com/in/kunalkolhe3/",},
                    )
                    st_profile_report(pr)
    app3.line_solid()
    
    app3.header('C) Model predictions and performance:')
    app3.text('Find the predictions on your data. <b>Press Predict button</b>.')
    st.sidebar.subheader('2. Predicted N2O with explainable AI:')
    with st.sidebar.expander('Click here to predict...', expanded=False): 
        if st.button("Predict"):    
            if analyzed_status == 1:   
                op_var, op_data, r2, mse, data_s = build_model(model, user_selected_data)
                analyzed_status, exp_ai = 0, 1
            elif analyzed_status == 2:
                op_var, op_data, r2, mse, data_s = build_model(model, sample_data)
                analyzed_status, exp_ai = 0, 0
            else:
                st.error('Unable to predict, Select data.')

    st.sidebar.info('''
            **Note:** Is application run slow ? _Computation time (sec.) depends on your data complexity with server run._
        ''')
    st.sidebar.markdown('''<small>ML App with Explainable AI v1.6 | Dec 2021</small> Copyright &copy; Kunal K.''', unsafe_allow_html=True)
   
    st.subheader('i) Output variable selection:')
    app3.text('A model is being built to predict the following <b>Y</b> variable:')
    st.info(op_var)
    st.subheader('ii) Model predictions:')
    
    tmp_download_link1 = download_link(op_data, 'predicted_data.csv', 'Click here to download predicted result file..!')
    st.markdown(tmp_download_link1, unsafe_allow_html=True)
   
    st.subheader('iii) Model perormance:')
    st.write('Model Accuracy Score (R2):', r2)
    st.write('Mean Squared Error (MSE) :', mse)
    st.text('Results are computed on your inputs and ML model (Xgb).')
    op_var, op_data, r2, mse = '', '', 0, 0
    app3.line_solid()

    app3.header('D) Explainable AI - Model prediction results:')
    st.info('Applicable for user data only, not for sample selected data.')
    if exp_ai == 1:
        app3.text('Predict the results with its explanation. Default record is selected 4th from provided data.')
        i = 4
        shap_summary_plot(data_s, model, i)
        exp_ai = 0
    else:
        pass
