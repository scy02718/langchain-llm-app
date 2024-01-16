import streamlit as st
import langchain_helper as lch

st.title("Pet name generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog"))

if animal_type == "Cat":
    pet_type = "cat"
else:
    pet_type = "dog"

names = lch.get_pet_names(pet_type)
st.write(names)