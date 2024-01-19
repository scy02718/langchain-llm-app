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
with open("const/word_list.txt", "r") as f:
    target_word = random.choice(f.readlines()).strip()
    # target_embedding = lms.get_word_embedding(target_word)


previous_guesses_list = []
guess_container = st.empty()
previous_guesses_container = st.empty()

print("what the fuck")

while True:
    print(previous_guesses_list)

    with previous_guesses_container.container():
        st.write("Previous Guesses:")
        for guess in previous_guesses_list:
            st.write(guess)

    with guess_container.container():
        key = random.randint(0, 100000)
        guess = st.text_input("Enter your guess:", key=key)
        submit = st.button("Submit", key=key+1)
        if submit and guess not in previous_guesses_list :
            previous_guesses_list.append(guess)
            print(previous_guesses_list)
            if guess == target_word:
                st.success("You got it!")
                break
        

    guess_container.empty()
    previous_guesses_container.empty()

