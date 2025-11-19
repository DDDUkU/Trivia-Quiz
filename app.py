import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Trivia Quiz",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Trivia Quiz")
st.success("Deployment test successful!")

# Test pandas functionality
try:
    df = pd.DataFrame({
        'Test': [1, 2, 3],
        'Data': ['A', 'B', 'C']
    })
    st.dataframe(df)
    st.success("Pandas is working!")
except Exception as e:
    st.error(f"Pandas error: {e}")
