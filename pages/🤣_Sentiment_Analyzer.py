import streamlit as st
import random
import util.chatAPI as lms

st.set_page_config(page_title="Sentiment Analyzer", page_icon="🤣")
st.title("Text Sentiment Analyzer")
st.write(
    """This page is a demo of the Text Sentiment Analyzer. It is a tool that can
    analyze the sentiment of a text, given a context. Try to be as detailed as you can be
    with the context."""
)

# Context Input
context_input = st.text_area("Enter the context as detailed as possible:")

# Text Input
text_input = st.text_area("Enter the text:")

# Submit Button
if st.button("Submit"):
    if context_input and text_input:
        sentiment_analysis = lms.analyze_sentiment(context_input, text_input)
        st.success(sentiment_analysis)
    else:
        st.warning("Please enter some text.")