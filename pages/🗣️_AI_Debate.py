import streamlit as st
import random
import util.chatAPI as lms

st.set_page_config(page_title="AI Debate", page_icon="🗣️")
st.title("AI Debate")
st.write(
    """This page is a demo of the AI Debate. It is a tool that will debate
    against you on any topic. It will try to convince you to agree with it."""
)

# Topic input
topic_input = st.text_input("Enter the topic:")

# Your opinion
opinion_input = st.text_area("Enter your opinion:")

# Submit Button
if st.button("Submit"):
    if topic_input and opinion_input:
        ai_opinion = lms.against_debate(topic_input, opinion_input)
        st.success(ai_opinion)
    else:
        st.warning("Please enter some text.")