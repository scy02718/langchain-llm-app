import streamlit as st
import util.googleAPI as lms

st.set_page_config(page_title="Poem Analyzer", page_icon="🖊️")
st.title("Poem Analyzer")
st.write(
    """This page is a demo of the Poem Analyzer. It is a tool that will 
    analyze any poems, and write high school level essays about the poem.
    You will be able to customize the number of paragraphs, total length, your age
    (to not make it suspicious), formality (from casual to formal), the overall topic of the essay,
    and finally the Language of the Essay as well!"""
)

col1, col2 = st.columns(2)

# Poem input
with col1:
    # Age Slider
    age = st.slider("Select your age:", 0, 100, 15)

    # Read const/languages_list.csv and get the list of languages
    languages = []
    with open("const/languages_list.csv", "r") as f:
        for line in f:
            languages.append(line.strip())
    
    # Language Selector
    language = st.selectbox("Select the language:", languages)

    # Formality Slider
    formality = st.slider("Select the formality:", 0.0, 1.0, 0.5, 0.1)

    # Topic Selector
    topic = st.text_input("Enter the topic of the essay:")

    # Paragraph Slider
    paragraphs = st.slider("Select the number of paragraphs:", 1, 5, 3)

    # Length Slider
    length = st.slider("Select the length of the essay:", 100, 2000, 500)
with col2:
    poem_input = st.text_area("Enter the poem:", height = 500)

# Submit Button
if st.button("Submit"):
    result = lms.poem_analyzer(poem_input, age, language, formality, topic, paragraphs, length)
    st.write(result)