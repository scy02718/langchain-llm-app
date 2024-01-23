import streamlit as st
import random
import util.googleAPI as lms

st.set_page_config(page_title="Algorithm Solver", page_icon="🤣")
st.title("Algorithm Solver")
st.write(
    """This page is a demo of the Algorithm Solver. It is a tool that can
    solve an algorithm problem with any selected language"""
)

# Choose the input programming language
input_language = st.selectbox("Select the input programming language:", ("Python", "Java", "C++", "C", "JavaScript", 
                                                                        "Go", "Kotlin", "PHP", "C#","Ruby", "Matlab")
                            )

# Enter the question
question = st.text_area("Enter the question:")

# Submit Button
if st.button("Submit"):
    if question and input_language:
        output_code = lms.solve_algorithm(question, input_language)
        st.success(output_code)
    else:
        st.warning("Please enter some code.")