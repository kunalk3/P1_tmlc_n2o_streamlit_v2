import streamlit as st
import hydralit_components as hc
import time
from apps import app3

def contact():
        col1, col2, col3 = st.columns(3)
    
    
        col1_exp = col1.expander('Linkedin proile')
        with col1_exp:
            # col1_exp.write('Connect me on')
            col1_exp.markdown('''<i>Connect me on 
                <a class="nav-link" href="https://www.linkedin.com/in/kunalkolhe3/" target="_blank">Linkedin</a></i>
            ''', unsafe_allow_html=True)
        col2_exp = col2.expander('Github proile')
        with col2_exp:
            col2_exp.markdown('''<i>Find me on 
                <a class="nav-link" href="https://github.com/kunalk3" target="_blank">Github</a></i>
            ''', unsafe_allow_html=True)
        col3_exp = col3.expander('Google proile')
        with col3_exp:
            col3_exp.markdown('''<i>Share your ideas on 
                <a class="nav-link" href="mailto:kunalkolhe333@gmail.com" target="_blank">Gmail</a></i>
            ''', unsafe_allow_html=True)

def app():
    st.write('''
            # __About me__
    ''')
    app3.text('Software Developer with 3.0 years of total industry experience in analytics, software design, and development.\
             Proficient in Python, C++, OOP, ML algorithms, data analytics with practical working experience in data analysis, planning \
             and designing, implementation, POC, releases to customers. Good analytical ability with a passion for turning data into \
             actionable insights, finding discoveries, hidden patterns, and solution through it.')
    
    app3.header('A) Connect with me:')
    with hc.HyLoader('Loading...',hc.Loaders.pulse_bars):
        time.sleep(1.5)
        contact()



