import streamlit as st
import random
import util.googleAPI as lms

st.set_page_config(page_title="Song Writer", page_icon="🧑‍🍳")
st.title("Song Writer")
st.write(
    """This page is a demo of the Song Writer. It is a tool that can
    generate a song for you, as well as the chord progression. You will choose the key, the topic of the lyrics,
    the genre of the music, the tempo of the music, and finally the structure of the music. You should also decide
    the complexity of the chord progression. 
    Then the AI will generate a song for you."""
)

input_key = st.selectbox("Select the key of the song:", ("C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"))
input_topic = st.text_input("Enter the topic of the song:")
input_genre = st.selectbox("Select the genre of the song:", ("Pop", "Rock", "Jazz", "Hip Hop", "Country", "Folk", "Ballad", "R&B"))
input_tempo = st.selectbox("Select the tempo of the song:", ("Slow", "Medium", "Fast"))
input_structure = st.selectbox("Select the structure of the song:", ("Verse-Chorus", "Verse-Chorus-Verse", "Verse-Chorus-Bridge-Chorus", "Verse-Verse-Chorus", "Other"))
if input_structure == "Other":
    input_structure = st.text_input("Enter the structure of the song:")
input_complexity = st.slider("Select the complexity of the chord progression:", 0, 100, 50)

# Submit Button
if st.button("Submit"):
    if input_topic:
        song = lms.song_writer(input_key, input_topic, input_genre, input_tempo, input_structure, input_complexity)
        st.success(song)
    else:
        st.warning("Please enter some topic.")
