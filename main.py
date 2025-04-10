import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_name_data():
    # Load the dataset from a CSV file
    df = pd.read_csv('https://raw.githubusercontent.com/gbean4/Post_2/9b874da1c45720f3196d7f1bd7edc4a60ee30484/fast_food_analysis.csv')    
    return df

df = load_name_data()

st.title("Fast Food Analysis")
st.write("This is a Streamlit app for analyzing economic data versus .")