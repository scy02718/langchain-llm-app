import streamlit as st
import random
import util.googleAPI as lms


if 'word_count' not in st.session_state:
    st.session_state.word_count = 0
if 'input_word_list' not in st.session_state:
    st.session_state.input_word_list = []
if 'word_list' not in st.session_state:
    with open('const/korean_word.txt', 'r', encoding='utf-8') as f:
        words = f.readlines()
        st.session_state.word_list = [word.strip() for word in words]
if 'num_hints' not in st.session_state:
    st.session_state.num_hints = 5

def get_word(last_word):
    last_letter = last_word[-1]
    # Find a word that starts with the last letter
    possible_words = [word for word in st.session_state.word_list if word[0] == last_letter and word not in st.session_state.input_word_list]
    if len(possible_words) == 0:
        return "No words found"
    else:
        # Randomly choose a word from the possible words
        word = random.choice(possible_words)
        return word[:-1] + "?"

def append_word(word, last_word):
    if word in st.session_state.input_word_list:
        st.error("The word has already been used.")
        return
    elif word not in st.session_state.word_list:
        st.error("The word does not exist.")
        return
    elif last_word != "" and word[0] != last_word[-1]:
        st.error("The word does not start with the correct letter.")
        return
    
    st.session_state.input_word_list.append(word)
    st.session_state.word_count += 1

    last_letter = word[-1]
    # Find a word that starts with the last letter
    possible_words = [word for word in st.session_state.word_list if word[0] == last_letter and word not in st.session_state.input_word_list]
    if len(possible_words) == 0:
        st.success("You won!")
    else:
        # Randomly choose a word from the possible words
        word = random.choice(possible_words)
        st.session_state.input_word_list.append(word)
        st.session_state.word_count += 1

st.set_page_config(page_title="Last Word Game", page_icon="🧑‍🍳")
st.title("Last Word Game")
st.write(
    """This page is a demo of the Last Word Game (끝말잇기). It is a game where
    you compete against a computer for the game, by providing a word that starts with the
    ending letter of the previous word."""
)

with st.container(height=400, border = False):
    col1, col2 = st.columns(2)
    if st.session_state.word_count >= 0:
            with col1:
                input_word = st.text_input("Enter the word:")
                last_word = st.session_state.input_word_list[-1] if st.session_state.input_word_list else ""
                st.write("The last word is: ", last_word)

                st.button("Submit", on_click=append_word, args=(input_word, last_word), type='primary')
                if st.session_state.num_hints > 0 and st.button("Hint") and last_word != "":
                        hint_word = get_word(last_word)
                        st.success(f'Hint : {hint_word}')
                        st.session_state.num_hints -= 1
                        st.write("You have ", st.session_state.num_hints, " hints left.")
                        
            with col2:
                with st.container(height=300, border = True):
                    if st.session_state.word_count > 0:
                        for i in range(st.session_state.word_count):
                            if i % 2 == 0:
                                st.success(st.session_state.input_word_list[i])
                            else:
                                st.warning(st.session_state.input_word_list[i])

