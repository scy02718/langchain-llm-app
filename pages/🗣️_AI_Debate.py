import streamlit as st
import util.googleAPI as lms

st.set_page_config(page_title="AI Debate", page_icon="🗣️")
st.title("AI Debate")
st.write(
    """This page is a demo of the AI Debate. It is a tool that will debate
    against you on any topic. It will try to convince you to agree with it.
    Another option is to have two AIs debate against each other, so that you can collect 
    ideas on both sides of the argument."""
)

# Topic input
topic_input = st.text_input("Enter the topic:")

# Select if you want to debate against an AI or have two AIs debate against each other
debate_type = st.radio("Select debate type:", ('AI vs AI', 'Against AI'))

if debate_type == 'Against AI':
    # Your opinion
    your_opinion = st.text_area("Enter your argument:")

    # Submit Button
    if st.button("Start"):
        if topic_input and your_opinion:
            ai_response = lms.ai_rebuttal(topic = topic_input, my_opinion = your_opinion)
            st.success(ai_response)
        else:
            st.warning("Please enter some text.")
else:
    # Split into two columns
    col1, col2 = st.columns(2)

    # AI 1 opinion
    with col1:
        ai1_opinion_input = st.text_area("Enter AI 1's opinion:")
    # AI 2 opinion
    with col2:
        ai2_opinion_input = st.text_area("Enter AI 2's opinion:")

    # Slider to select how many times to repeat the debate
    repeat = st.slider("Select how many conversations the AI should do each:", 1, 10, 1)
    
    # Submit Button
    if st.button("Submit"):
        if topic_input and ai1_opinion_input and ai2_opinion_input:
            ai1_previous_arguments = []
            ai2_previous_arguments = []

            for i in range(repeat):
                ai1_argument = lms.ai_debate(topic = topic_input, my_opinion = ai1_opinion_input, opponent_opinion=ai2_opinion_input,
                                                        my_arguments = ai1_previous_arguments, opponents_arguments = ai2_previous_arguments)
                ai1_previous_arguments.append(ai1_argument)
                st.success(ai1_argument)

                ai2_argument = lms.ai_debate(topic = topic_input, my_opinion = ai2_opinion_input, opponent_opinion=ai1_opinion_input,
                                                        my_arguments = ai2_previous_arguments, opponents_arguments = ai1_previous_arguments)
                ai2_previous_arguments.append(ai2_argument)
                st.warning(ai2_argument)
        else:
            st.warning("Please enter some text.")