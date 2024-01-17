import streamlit as st
import random
import util.chatAPI as lms

st.set_page_config(page_title="Sentiment Modifier", page_icon="🙂")
st.title("Text Sentiment Modifier")
st.write(
    """This page is a demo of the Text Sentiment Modifier. It is a tool that can
    modify the tone and sentiment of a text, without modifying the content of the text."""
)

# Text Input
text_input = st.text_area("Enter your text:")

# Slider for Strength
strength = st.slider("Select the strength of the sentiment:", 0.0, 10.0, 5.0, step=0.1)

# Create two columns
col1, col2 = st.columns(2)

# Tone Buttons
with col1:
    selected_tone = st.radio("Select tone:", ('Formal', 'Casual', 'Polite', 'Impolite', 'Sarcastic'))

# Sentiment Buttons
with col2:
    selected_sentiment = st.radio("Select sentiment:", ('Happy', 'Sad', 'Angry', 'Neutral'))

# Length of the output text slider
text_length = st.slider("Select the maximum length of the output text:", 10, 500, 50, key = "text_length")

# Submit Button
if st.button("Submit"):
    if text_input:
        modified_text = lms.modify_sentiment(text_input, selected_tone, selected_sentiment, strength, text_length)
        st.success(modified_text)
    else:
        st.warning("Please enter some text.")