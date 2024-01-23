import streamlit as st
import random
import util.googleAPI as lms

st.set_page_config(page_title="Code Translator", page_icon="🤣")
st.title("Code Translator")
st.write(
    """This page is a demo of the Code Translator. It is a tool that can
    translate a code in one language to another, keeping the behaviour of the code as similar as possible."""
)

col1, col2 = st.columns(2)

with col1:
    # Choose the input programming language
    input_language = st.selectbox("Select the input programming language:", ("Python", "Java", "C++", "C", "JavaScript", 
                                                                            "Go", "Kotlin", "PHP", "C#","Ruby", "Matlab")
                                )
with col2:
    # Choose the output programming language
    output_language = st.selectbox("Select the output programming language:", ("Python", "Java", "C++", "C", "JavaScript", 
                                                                            "Go", "Kotlin", "PHP", "C#","Ruby", "Matlab")
                                )

# Choose the input code
input_code = st.text_area("Enter the input code:")

# Submit Button
if st.button("Submit"):
    if input_code:
        output_code = lms.translate_code(input_code, input_language, output_language)
        st.success(output_code)
    else:
        st.warning("Please enter some code.")