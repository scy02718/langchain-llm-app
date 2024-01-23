import streamlit as st
import random
import util.googleAPI as lms

# Session states for all modes
if 'quiz_settings' not in st.session_state:
    st.session_state.quiz_settings = None
if 'answer_changed' not in st.session_state:
    st.session_state.answer_changed = False

# Session states for sentence translation
if 'sentence_translation' not in st.session_state:
    st.session_state.sentence_translation = 0
if 'sentence_list' not in st.session_state:
    st.session_state.sentence_list = ""
if 'sentence_answer_list' not in st.session_state:
    st.session_state.answer_list = None

# Session states for vocabulary test
if 'vocabulary_test' not in st.session_state:
    st.session_state.vocabulary_test = 0
if 'word_list' not in st.session_state:
    st.session_state.word_list = ""
if 'word_answer_list' not in st.session_state:
    st.session_state.answer_list = None

# Session states for conversational AI
if 'conversational_ai' not in st.session_state:
    st.session_state.conversational_ai = 0
if 'user_input_list' not in st.session_state:
    st.session_state.user_input_list = []
if 'ai_response_list' not in st.session_state:
    st.session_state.ai_response_list = []

def set_session_state(state_name, state_value):
    st.session_state[state_name] = state_value
def set_quiz_settings(mode, language, level, num):
    st.session_state.quiz_settings = {
        "mode": mode,
        "language": language,
        "level": level,
        "num": num
    }
def answer_changed():
    st.session_state.answer_changed = True
def reset_session_state():
    st.session_state.quiz_settings = None
    st.session_state.sentence_translation = 0
    st.session_state.sentence_list = ""
    st.session_state.sentence_answer_list = None
    st.session_state.answer_changed = False
    st.session_state.vocabulary_test = 0
    st.session_state.word_list = ""
    st.session_state.word_answer_list = None
    st.session_state.conversational_ai = 0
    st.session_state.user_input_list = None
    st.session_state.ai_response_list = None


def sentence_translation(): 
    if st.session_state.sentence_translation == 1:
        language = st.session_state.quiz_settings["language"]
        level = st.session_state.quiz_settings["level"]
        num = st.session_state.quiz_settings["num"]

        if st.session_state.sentence_list == "":
            sentences = lms.get_sentence(language, level, num)
            sentences = sentences.split("\n")

            set_session_state("sentence_list", sentences)
        else:
            sentences = st.session_state.sentence_list

        for i in range(num):
            sentence = sentences[i]
            st.write(sentence)

        input_answer = st.text_area("Enter the translation: It should be in 1. Translation for sentence 1, 2. Translation for sentence 2, etc.", on_change=answer_changed())

        if st.session_state.answer_changed:
            answers = input_answer.split("\n")
            set_session_state("sentence_answer_list", answers)

            st.button("Submit", on_click = set_session_state, args = ("sentence_translation", 2))
    if st.session_state.sentence_translation == 2:
        language = st.session_state.quiz_settings["language"]
        level = st.session_state.quiz_settings["level"]

        sentences = st.session_state.sentence_list
        answers = st.session_state.sentence_answer_list

        col1, col2 = st.columns(2)
        with col1:
            st.success("Sentences:")
            for sentence in sentences:
                st.success(sentence)
        with col2:
            st.warning("Answers:")
            for answer in answers:
                st.warning(answer)
        
        evaluation = lms.evaluate_translation(sentences, answers, language,level)
        st.success(evaluation)

        st.button("Restart", on_click = reset_session_state)

def vocabulary_test():
    if st.session_state.vocabulary_test == 1:
        language = st.session_state.quiz_settings["language"]
        level = st.session_state.quiz_settings["level"]
        num = st.session_state.quiz_settings["num"]

        if st.session_state.word_list == "":
            words = lms.get_words(language, level, num)
            words = words.split("\n")

            set_session_state("word_list", words)
        else:
            words = st.session_state.word_list

        for i in range(num):
            word = words[i]
            st.write(word)

        input_answer = st.text_area("Enter the translation: It should be in 1. Translation for word 1, 2. Translation for word 2, etc.", on_change=answer_changed())

        if st.session_state.answer_changed:
            answers = input_answer.split("\n")
            set_session_state("word_answer_list", answers)

            st.button("Submit", on_click = set_session_state, args = ("vocabulary_test", 2))
    if st.session_state.vocabulary_test == 2:
        language = st.session_state.quiz_settings["language"]
        level = st.session_state.quiz_settings["level"]

        words = st.session_state.word_list
        answers = st.session_state.word_answer_list

        col1, col2 = st.columns(2)
        with col1:
            st.success("Words:")
            for word in words:
                st.success(word)
        with col2:
            st.warning("Answers:")
            for answer in answers:
                st.warning(answer)
        
        evaluation = lms.evaulate_words(words, answers, language,level)
        st.success(evaluation)

        st.button("Restart", on_click = reset_session_state)

def conversational_ai():
    print(st.session_state.conversational_ai)

    if st.session_state.conversational_ai >= 1:
        col1, col2 = st.columns(2)
        with col1:
            language = st.session_state.quiz_settings["language"]
            input_sentence = st.text_input("Enter the sentence:", on_change=answer_changed())

            if st.session_state.answer_changed:
                st.session_state.user_input_list.append(input_sentence)

                user_input_list = st.session_state.user_input_list
                ai_response_list = st.session_state.ai_response_list

                st.button("Submit", on_click = set_session_state, args = ("conversational_ai", 2))
        with col2:
            st.write("Conversation:")
            for i in range(len(user_input_list)):
                st.success(f"User: {user_input_list[i]}")


st.set_page_config(page_title="Language Perfect", page_icon="📷")
st.title("Language Perfect")
st.write(
    """This page is a demo of Language Perfect. It is a tool that can
    help people learn language with a help of language model. There are number of modes of the app.
    Firstly, sentence translation. There will be number of sentences in the language that you choose. 
    You will have to translate that to english and submit, in which the model will tell you how well you did, and 
    a good example of the translation. Secondly, there is a vocabulary test. There will be number of words generated by the 
    AI, and you will have to translate them. Thirdly, there is a conversational AI. You can freely talk to the AI, and it will give
    two answers. Firstly, it will give you a response to whatever you said, it the chosen language. Secondly, it will give you
    feedback on what you said, such as any grammatical errors, or any words that you could have used instead. Enjoy!"""
)

# Choose the language
with open("const/languages_list.csv", "r") as f:
    languages = []
    for line in f:
        if line.strip() != "English":
            languages.append(line.strip())

if st.session_state.sentence_translation == 0:
    language = st.selectbox("Select the language:", languages)

    mode = st.selectbox("Select the mode:", ("Sentence Translation", "Vocabulary Test", "Conversational AI"))

    # Choose your level 
    level = st.selectbox("Select your level:", ("Beginner", "Intermediate", "Advanced"))

    if mode == "Sentence Translation":
        # Choose the number of sentences
        num = st.slider("Select the number of sentences:", 2, 10, 5)
        start = st.button("Start", on_click = set_session_state, args = ("sentence_translation", 1))
    elif mode == "Vocabulary Test":
        # Choose the number of words
        num = st.slider("Select the number of words:", 1, 10, 5)
        start = st.button("Start", on_click = set_session_state, args = ("vocabulary_test", 1))
    elif mode == "Conversational AI":
        num = 0
        start = st.button("Start", on_click = set_session_state, args = ("conversational_ai", 1))
        
    set_quiz_settings(mode, language, level, num)


sentence_translation()  
vocabulary_test()
conversational_ai()