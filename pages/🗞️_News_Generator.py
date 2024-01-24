import streamlit as st
import random
import util.googleAPI as lms

st.set_page_config(page_title="News Generator", page_icon="🧑‍🍳")
st.title("News Generator")
st.write(
    """This page is a demo of the News Generator. It is a tool that can
    generate a attractive news title and news article based on the topic that you want.
    You can decide the length of the article, the topic of the article, how creative you want the
    content to be, the attrativeness of the title, and the sentiment of the article. """
)

input_topic = st.text_input("Enter the topic:")
input_length = st.selectbox("Select the length of the article:", ("Short", "Medium", "Long"))
# Creativity should be between 0 and 1, with 0 being the least creative and 1 being the most creative
input_creativity = st.slider("Select the creativity of the article:", 3, 100, 50)
input_attractiveness = st.slider("Select the attractiveness of the title:", 0, 100, 50)
input_sentiment = st.selectbox("Select the sentiment of the article:", ("Positive", "Neutral", "Negative"))

# Submit Button
if st.button("Submit"):
    if input_topic:
        article = lms.news_generator(input_topic, input_length, input_creativity / 100, input_attractiveness, input_sentiment)
        st.success(article)
    else:
        st.warning("Please enter some topic.")
