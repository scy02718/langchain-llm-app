import streamlit as st
import random
import util.googleAPI as lms

st.set_page_config(page_title="Recipe Generator", page_icon="🤣")
st.title("Recipe Generator")
st.write(
    """This page is a demo of the Recipe Generator. It is a tool that can
    generate a recipe based on the ingredients that you have, as well as your
    skill level, the time you have, and the type of cuisine you want, and the time of the day.
    Finally, you can also choose the nutrition you want, such as low carb, high protein, etc."""
)

input_ingredients = st.text_area("Enter the ingredients:")
input_skill_level = st.selectbox("Select your skill level:", ("Beginner", "Intermediate", "Advanced"))
input_time = st.selectbox("Select the time you have:", ("< 30 minutes", "30 - 60 minutes", "> 60 minutes"))
input_cuisine = st.selectbox("Select the cuisine you want:", ("American", "Chinese", "French", "Indian", "Italian", "Japanese", "Korean", "Mexican", "Thai", "Vietnamese"))
input_time_of_day = st.selectbox("Select the time of the day:", ("Breakfast", "Lunch", "Dinner"))
input_nutrition = st.selectbox("Select the nutrition you want:", ("Low Carb", "High Protein", "Low Fat", "Low Calorie", "Low Sodium", "Low Sugar", "Balanced"))

# Submit Button
if st.button("Submit"):
    if input_ingredients:
        recipe = lms.recipe_generator(input_ingredients, input_skill_level, input_time, input_cuisine, input_time_of_day, input_nutrition)
        st.success(recipe)
    else:
        st.warning("Please enter some ingredients.")
