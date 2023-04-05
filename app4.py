 
    
import streamlit as st
from PIL import Image

st.title("DepreWizard App")

st.camera_input('rrr')

Cost = st.number_input("What is the cost of the Asset in N")
Scrap_value = st.number_input("What is the estimated scrap_value of the Asset in N")
Useful_life = st.number_input("What is the estimated useful_life of the Asset in years")

def Cal_Annual_depreciation(Cost, Scrap_value, Useful_life):

    depreciation_value = Cost - Scrap_value
    Annual_depreciation = depreciation_value/Useful_life

    return f'The Annual_depreciation of the Fixed Asset is {Annual_depreciation}'

if st.button("Calculate Depreciation"):
    st.write(Cal_Annual_depreciation(Cost, Scrap_value, Useful_life))
