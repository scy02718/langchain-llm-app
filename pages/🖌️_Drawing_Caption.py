import streamlit as st
import random
import util.googleAPI as lms
import numpy as np
from streamlit_drawable_canvas import st_canvas
from PIL import Image


st.set_page_config(page_title="Drawing Caption", page_icon="🤣")
st.title("Drawing Caption")
st.write(
    """This page is a demo of drawing caption. It is a where the user
     can freely draw on the canvas, and AI will generate a caption
     based on the drawing, describing what is present on the drawing. It can also
     analyze the drawing, and tell the user the deeper meaning of the drawing"""
)

# Define a canvas where the user can draw
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:",
    ("FREEDRAW", "LINE", "RECT", "CIRCLE", "TRANSFORM", "POLYGON", "POINT"),
)
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode.lower() == "point":
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=500,
    drawing_mode=drawing_mode.lower(),
    point_display_radius=point_display_radius if drawing_mode.lower() == "point" else 0,
    display_toolbar=st.sidebar.checkbox("Display toolbar", True),
    key="full_app",
)

col1, col2 = st.columns(2)

with col1:
    caption = st.button("Caption")
with col2:
    analyze = st.button("Analyze")


# Do something interesting with the image data and paths
if caption:
    pil_image = Image.fromarray(canvas_result.image_data)
    pil_image = pil_image.convert('RGB')

    drawing_caption = lms.paint_captioning(pil_image)
    st.success(drawing_caption)

if analyze:
    pil_image = Image.fromarray(canvas_result.image_data)
    pil_image = pil_image.convert('RGB')

    drawing_caption = lms.paint_analysis(pil_image)
    st.success(drawing_caption)