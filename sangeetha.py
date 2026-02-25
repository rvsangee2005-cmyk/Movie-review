import streamlit as st
from transformers import pipeline

# Load model
sentiment = pipeline("sentiment-analysis")

st.title("🎬 Movie Review Sentiment Analyzer")

user_input = st.text_area("Enter a movie review")

if st.button("Analyze"):
    if user_input:
        result = sentiment(user_input)
        st.write("Sentiment:", result[0]["label"])
        st.write("Confidence:", round(result[0]["score"], 2))
    else:
        st.write("Please enter a review")