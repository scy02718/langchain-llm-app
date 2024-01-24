import streamlit as st
import random
import util.googleAPI as lms

st.set_page_config(page_title="Teaching Planner", page_icon="🧑‍🍳")
st.title("Teaching Planner")
st.write(
    """This page is a demo of the Teaching Planner. It is a tool that can
    generate a teaching planner. It will generate a teaching planner based on the topic that you want to teach.
    You will choose the length of the lesson, the topic of the lesson, the age and level of the students, the
    type of the lesson, and the style of the lesson. You will also choose how creative the lesson should be.
    Then an AI model will generate a detailed teaching planner for you, which will have record and planning
    for every minute of the lesson. """
)

input_topic = st.text_input("Enter the topic:")
input_length = st.slider("Select the length of the lesson, in minutes:", 30, 120, 60)
input_age = st.selectbox("Select the age of the students:", ("3 - 6", "7 - 12", "13 - 18", "19 - 25", "26 - 35", "36 - 50", "51 - 65", "65+"))
input_level = st.selectbox("Select the level of the students:", ("Beginner", "Intermediate", "Advanced"))
input_type = st.selectbox("Select the type of the lesson:", ("Online", "In Person"))
input_style = st.selectbox("Select the style of the lesson:", ("Lecture", "Discussion", "Group Work", "Individual Work", "Presentation", "Game"))
input_creativity = st.slider("Select the creativity of the lesson:", 3, 100, 50)

# Submit Button
if st.button("Submit"):
    if input_topic:
        lesson = lms.teaching_planner(input_topic, input_length, input_age, input_level, input_type, input_style, input_creativity / 100)
        st.success(lesson)
    else:
        st.warning("Please enter some topic.")
