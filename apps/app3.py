import streamlit as st

# Header style
def header(url):
     st.markdown(f'<p style="color:#FFA500; font-size:27px; background-color:1a1a1a; border-radius:2%;">{url}</p>', unsafe_allow_html=True)

# Text 
def text(url):
     st.markdown(f'<p style="color:#808080; font-size:18px; background-color:1a1a1a; border-radius:2%;">{url}</p>', unsafe_allow_html=True)

# Subtext
def sub_text(url):
     st.markdown(f'<p style="color:#808080; font-size:22px; background-color:1a1a1a; border-radius:2%;">{url}</p>', unsafe_allow_html=True)

# Solid line style
def line_solid():
     st.markdown(f'<hr style="height:2px; width:90%; color:SlateBlue; background-color:SlateBlue; border-width:0; margin-left:auto; margin-right:auto;">', unsafe_allow_html=True)

# Dashed line style
def line_dash():
     st.markdown(f'<hr style="border:1.5px solid SlateBlue">', unsafe_allow_html=True)

