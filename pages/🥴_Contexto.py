import streamlit as st
import random
import util.googleAPI as lms
import numpy as np

st.set_page_config(page_title="Contexto", page_icon="🤣")
st.title("Contexto")
st.write(
    """This page is a demo of Contexto. It is a game that the user
    tries to guess the word. The user will continuously input a word, and the AI will
    determine the contextual similartiy between the word and the target word. """
)

# Define target word
with open("const/word_embeddings.csv", "r") as f:
    words = f.readlines()
    target_word = random.choice(words).split(",")
    word = target_word[0]
    embedding = target_word[1:]

    # Remove [ and ] from the embedding
    embedding[0] = embedding[0][1:]
    embedding[-1] = embedding[-1][:-2]
    
    embedding = np.array(embedding).astype(float)

# Display the target word
st.write("The target word is: ", word)

# Define the input word
input_word = st.text_input("Enter the word:")

# Submit Button
if st.button("Submit"):
    if input_word:
        input_embedding = lms.get_word_embedding(input_word)
        # Calculate cosine similarity between embeddings
        similarity = np.dot(input_embedding, embedding)/(np.linalg.norm(input_embedding)*np.linalg.norm(embedding))
        # Embedding size is different!
        st.success(similarity)
    else:
        st.warning("Please enter some code.")