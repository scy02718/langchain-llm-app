import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_stage(stage):
    st.session_state.stage = stage

# Some code
st.button('First Button', on_click=set_stage, args=(1,))

if st.session_state.stage > 0:
    # Some code
    st.button('Second Button', on_click=set_stage, args=(2,))
if st.session_state.stage > 1:
    # More code, etc
    st.button('Third Button', on_click=set_stage, args=(3,))
if st.session_state.stage > 2:
    st.write('The end')
st.button('Reset', on_click=set_stage, args=(0,))