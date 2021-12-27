ines (69 sloc)  5.78 KB
   
<div align="right">
<img src="https://user-images.githubusercontent.com/41562231/141720820-090897f9-f564-45e2-9265-15c1269db795.png" height="120" width="900">
</div>

# __N2O predictions application with Explainable AI__
This repository is a part of TMLC project with end-to-end machine learning pipeline with deployment using PaaS on streamlit. Here, we have use the concept of __Explainable AI__ in which whatever the ML application predicts, we are able to see _real time input values with its feature contributions, its impact on model, behaviour and summary_ in detail with.

__Project title:__ Machine learning improves predictions of an Agricultural Nitrous Oxide (N2O) emissions from intensively managed cropping systems.

- _For N2O predictions, we have used ML model with __Xgb regressor__ algorithm and for user data analysis, wo go with __Auto EDA__ (pandas_profiling tool). Application is integrated using __Hydralit__ package for responsive and animated navbar, theme components in deployment using __streamlit__._
- An idea with data is taken from a __published paper__ in _Environmental Research [Research Paper](https://iopscience.iop.org/article/10.1088/1748-9326/abd2f3) (Paper published 19 January 2021)_

<div align="center">
  <a href="https://github.com/kunalk3/P1_tmlc_n2o_streamlit_v2/issues"><img src="https://img.shields.io/github/issues/kunalk3/workiing_with_text_data_scraping" alt="Issues Badge"></a>
  <a href="https://github.com/kunalk3/P1_tmlc_n2o_streamlit_v2/graphs/contributors"><img src="https://img.shields.io/github/contributors/kunalk3/workiing_with_text_data_scraping?color=872EC4" alt="GitHub contributors"></a>
  <a href="https://www.python.org/downloads/release/python-390/"><img src="https://img.shields.io/static/v1?label=python&message=v3.9&color=faff00" alt="Python 3.9"</a>
  <a href="https://github.com/kunalk3/P1_tmlc_n2o_streamlit_v2/blob/main/LICENSE"><img src="https://img.shields.io/github/license/kunalk3/workiing_with_text_data_scraping?color=019CE0" alt="License Badge"/></a>
  <a href="https://github.com/kunalk3/P1_tmlc_n2o_streamlit_v2g"><img src="https://img.shields.io/badge/lang-eng-ff1100"></img></a>
  <a href="https://github.com/kunalk3/P1_tmlc_n2o_streamlit_v2"><img src="https://img.shields.io/github/last-commit/kunalk3/workiing_with_text_data_scraping?color=309a02" alt="GitHub last commit">
</div>
  
<div align="center">   
  
  [![Windows](https://img.shields.io/badge/WindowsOS-000000?style=flat-square&logo=windows&logoColor=white)](https://www.microsoft.com/en-in/)
  [![Visual Studio Code](https://img.shields.io/badge/VSCode-0078d7.svg?style=flat-square&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
  [![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?style=flat-square&logo=Jupyter&logoColor=white)](https://jupyter.org/)
  [![Pycharm](https://img.shields.io/badge/Pycharm-41c907.svg?style=flat-square&logo=Pycharm&logoColor=white)](https://www.jetbrains.com/pycharm/)
  [![Colab](https://img.shields.io/badge/Colab-F9AB00.svg?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/?utm_source=scs-index/)
  [![Spyder](https://img.shields.io/badge/Spyder-838485.svg?style=flat-square&logo=spyder%20ide&logoColor=white)](https://www.spyder-ide.org/)
  [![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg?style=flat-square&logo=spyder%20ide&logoColor=white)](https://share.streamlit.io/)
</div>
  
<div align="center">
  
  [![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0078d7)](https://www.linkedin.com/in/kunalkolhe3/)
  [![Github Badge](https://img.shields.io/badge/Github-Profile-informational?style=flat&logo=github&logoColor=white&color=black)](https://github.com/kunalk3/)
  [![Gmail Badge](https://img.shields.io/badge/Gmail-Profile-informational?style=flat&logo=Gmail&logoColor=white&color=e44e4e)](mailto:kunalkolhe333@gmail.com)
  [![Facebook Badge](https://img.shields.io/badge/Facebook-Profile-informational?style=flat&logo=facebook&logoColor=white&color=0078d7)](https://www.facebook.com/kunal.kolhe.98/)
  [![Instagram Badge](https://img.shields.io/badge/Instagram-Profile-informational?style=flat&logo=Instagram&logoColor=white&color=c90076)](https://www.instagram.com/kkunalkkolhe/)
</div>
  
---
  
## :wrench: Installation
- Create __virtual environment__ `python -m venv VIRTUAL_ENV_NAME` and activate it `.\VIRTUAL_ENV_NAME\Scripts\activate`.
- Install necessary library for this project from the file `requirements.txt` or manually install by `pip`.
  ```
  pip install -r requirements.txt
  ```
  To create project library requirements, use below command,
  ```
  pip freeze > requirements.txt
  ```
- Libraries that are used in this project (highlighted few)
    ```python
    import pandas as pd
    import matplotlib.pyplot as plt
    import streamlit as st
    import streamlit.components.v1 as components
    import shap
    from sklearn.metrics import r2_score, mean_squared_error
    from pandas_profiling import ProfileReport
    from streamlit_pandas_profiling import st_profile_report
    import pybase64, joblib
    ```
---
  
- Run app.py using below command to start streamlit API
  ``` 
  streamlit run app.py
  ```
- By default, streamlit will run on port 8501 locally.
  
  Local URL: http://localhost:8501

  Network URL: http://192.168.0.102:8501
  
---  

## :bulb: Demo
#### :bookmark: _Output_ - 
https://user-images.githubusercontent.com/41562231/147125518-2f7c95b7-720b-4d80-ac04-dae671cf4caa.mp4

---  
  
## :bookmark: Directory Structure 
```bash
    .                                               # Root directory
    ├── data                                        # Input data directory
    │   ├── Dataset.csv                             # Dataset used for Xgb model
    │   ├── sample_data.csv                         # Sample input data
    ├── Model                                       # Model directory
    │   ├── model_xgb_61_final.joblib.compressed    # Model (Xgb regressor)
    ├── apps                                        # Application directory
    │   ├── app1.py                                 # Single prediction with AI
    │   ├── app2.py                                 # Predictions on user data with AI
    │   ├── app3.py                                 # UI enhancement
    │   ├── app4.py                                 # Connect page
    ├── .streamlit                                  # Streamlit theme param directory
    │   ├── config.toml                             # Configurarion theme file
    ├── requirements.txt                            # Project requirements library with versions
    ├── README.md                                   # Project README file
    └── LICENSE                                     # Project License file
```
---  

## :cloud: Live Application
__Live Aplication__ is running on streamlit cloud platform, you can access from below.
  
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/kunalk3/p1_tmlc_n2o_streamlit_v2/main/app.py)
  
---
  
### :iphone: Connect with me
`You say freak, I say unique. Don't wait for an opportunity, create it.`
  
__Let’s connect, share the ideas and feel free to ping me...__
  
<div align="center"> 
  <p align="left">
    <a href="https://linkedin.com/in/kunalkolhe3" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg" alt="kunalkolhe3" height="30" width="40"/></a>
    <a href="https://github.com/kunalk3/" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="kunalkolhe3" height="30" width="40"/></a>
    <a href="https://fb.com/kunal.kolhe.98" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/facebook.svg" alt="kunal.kolhe.98" height="30" width="40"/></a>
    <a href="mailto:kunalkolhe333@gmail.com" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/gmail.svg" alt="kunalkolhe333" height="30" width="40"/></a>
    <a href="https://instagram.com/kkunalkkolhe" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/instagram.svg" alt="kkunalkkolhe" height="30" width="40"/></a>
    <a href="https://www.hackerrank.com/kunalkolhe333" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/hackerrank.svg" alt="kunalkolhe333" height="30" width="40"/></a>
  </p>
</div>
  
<div align="left">
<img src="https://user-images.githubusercontent.com/41562231/141720940-53eb9b25-777d-4057-9c2d-8e22d2677c7c.png" height="120" width="900">
</div>
