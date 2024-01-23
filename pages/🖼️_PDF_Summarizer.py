import streamlit as st
import random
import util.googleAPI as lms
import PIL.Image as Image
import cv2
import numpy as np
import PyPDF2

st.set_page_config(page_title="PDF Summarizer", page_icon="📷")
st.title("PDF Summarizer")
st.write(
    """This page is a demo of the Visual Captioning tool. It is a tool that can
    summarize lecture and notes, into an understandable notes."""
)

col1, col2 = st.columns(2)

with col1:
    # Image Input
    pdf_input = st.file_uploader("Upload PDF:", type=["pdf"])

    # Question about the image
    question = st.text_input("(Optional) Enter a question about the lecture:")

    if st.button("Submit"):
        with col2:
            if pdf_input is not None:
                # Read the PDF file
                pdf_reader = PyPDF2.PdfReader(pdf_input)

                content = []
                for page in range(len(pdf_reader.pages)):
                    content += pdf_reader.pages[page].images

                for i in range(len(content)):
                    st.image(Image(content[i]))

            else:
                st.warning("Please upload an image.")
