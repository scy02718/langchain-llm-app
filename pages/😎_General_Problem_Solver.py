import streamlit as st
import random
import util.googleAPI as lms

st.set_page_config(page_title="Problem Solver", page_icon="🤣")
st.title("General Problem Solver")
st.write(
    """This page is a demo of the General Problem Solver. It is a tool that can
    solve any problem that you have, by having an AI creating a prompt for another AI input.
    This will mean the problem will be generalized and solved."""
)

input_problem = st.text_area("Enter the problem:")

# Submit Button
if st.button("Submit"):
    if input_problem:
        prompt = lms.create_prompt(input_problem)
        st.success(prompt)
    else:
        st.warning("Please enter some code.")