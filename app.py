import streamlit as st
st.set_page_config(layout='wide', initial_sidebar_state='auto', page_title='Dev:Kunal K')
import hydralit_components as hc
import time
from apps import app1, app2, app3, app4

menu_data = [
        {'id': '1', 'icon': "fas fa-tachometer-alt", 'label':"Single record"},
        {'id': '2', 'icon':"far fa-clone",'label':"User data"},
        {'id': '3', 'icon': "far fa-address-book", 'label':"Contact"}] 

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(sticky_nav=True, sticky_mode='pinned', menu_definition=menu_data, override_theme=over_theme,
            home_name='Home', login_name='This is a guest profile', use_animation=True, hide_streamlit_markers=True)

def get_id():
    return menu_id

def home_data():
    st.write('''
            # __N2O Prediction App with Explainable AI__
    ''')
    app3.sub_text('<b>Machine learning improves predictions of an Agricultural Nitrous Oxide (N2O) emissions from intensively managed cropping systems.</b> \
        <i>In this implementation, app is built on a regression model using XgBoost algorithm</i>.')
    app3.line_solid()

current_menu_id = get_id()

if current_menu_id == '2':
    app2.app()
elif current_menu_id == '1':
    app1.app()
elif current_menu_id == '3':
    app4.app()
else:
    with hc.HyLoader('Loading the application...',hc.Loaders.pulse_bars):
        time.sleep(1.5)
        home_data()

