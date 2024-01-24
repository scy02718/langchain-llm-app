import streamlit as st
import random
import util.googleAPI as lms

st.set_page_config(page_title="Plot Writer", page_icon="🧑‍🍳")
st.title("Plot Writer")
st.write(
    """This page is a demo of the Plot Writer. It is a tool that can
    generate a plot for a story. You can choose the target audience, genre of the story,
    the type of the story (drama, book, movie, etc.), the length of the story, if it is happy ending or not,
    and the sentiment of the story. You will also provide vague plot of how the story proceeds, and some description of the main characters.
    The AI will then generate a detailed plot for you."""
)

input_target_audience = st.selectbox("Select the target audience:", ("Children", "Teenagers", "Adults", "Elderly"))
input_genre = st.selectbox("Select the genre:", ("Action", "Adventure", "Comedy", "Crime", "Drama", "Fantasy", "Historical", "Horror", "Mystery", "Romance", "Science Fiction", "Thriller", "Western"))
input_type = st.selectbox("Select the type of the story:", ("Book", "Drama", "Movie", "TV Show", "Play", "Musical", "Game", "Other"))
input_length = st.selectbox("Select the length of the story:", ("Short", "Medium", "Long"))
input_ending = st.checkbox("Happy Ending")
input_ending = "Happy" if input_ending else "Sad"
input_sentiment = st.selectbox("Select the sentiment of the story:", ("Positive", "Neutral", "Negative"))

input_plot = st.text_area("Enter the plot: The plot should be a vague description of how the story proceeds")
input_characters = st.text_area("Enter the characters: ")

if st.button("Submit"):
    if input_plot and input_characters:
        plot = lms.plot_writer(input_target_audience, input_genre, input_type, input_length, input_ending, input_sentiment, input_plot, input_characters)
        st.success(plot)
    else:
        st.warning("Please enter some plot and characters.")



