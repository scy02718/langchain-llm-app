import streamlit as st
import random
import util.googleAPI as lms
import PIL.Image as Image
import cv2
import numpy as np

def get_captions_every_n_seconds(vid, n):
    vidcap = cv2.VideoCapture(vid) # load video from disk
    cur_frame = 0
    success = True
    
    frame_rate = vidcap.get(cv2.CAP_PROP_FPS) # get frame rate
    num_frames_ns = int(frame_rate * n) # get number of frames in n seconds
    num_frame = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)) # get number of frames in video

    captions = []

    # Progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()

    while cur_frame < num_frame and success:
        success, frame = vidcap.read() # get next frame from video
        if cur_frame % num_frames_ns == 0:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(frame)

            # Get the caption
            caption = lms.image_captioning(pil_img)
            captions.append(caption)
        cur_frame += 1

        # Update progress bar
        progress_bar.progress(cur_frame / num_frame)
        status_text.text(f"{100 * cur_frame/num_frame}% complete")

    return captions
def get_answers_every_n_seconds(vid, question, n):
    vidcap = cv2.VideoCapture(vid) # load video from disk
    cur_frame = 0
    success = True
    
    frame_rate = vidcap.get(cv2.CAP_PROP_FPS) # get frame rate
    num_frames_ns = int(frame_rate * n) # get number of frames in n seconds
    num_frame = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)) # get number of frames in video

    captions = []

    # Progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()

    while cur_frame < num_frame and success:
        success, frame = vidcap.read() # get next frame from video
        if cur_frame % num_frames_ns == 0:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(frame)

            # Get the caption
            caption = lms.image_questioning(pil_img, question)
            captions.append(caption)
        cur_frame += 1

        # Update progress bar
        progress_bar.progress(cur_frame / num_frame)
        status_text.text(f"{100 * cur_frame/num_frame}% complete")

    return captions

st.set_page_config(page_title="Visual Captioning", page_icon="📷")
st.title("Visual Captioning")
st.write(
    """This page is a demo of the Visual Captioning tool. It is a tool that can
    caption both images and videos. Video captioning will take a lot of time, and
    still on research."""
)

col1, col2 = st.columns(2)

with col1:
    # Select the type of input, image or video
    input_type = st.radio("Select the type of input:", ('Image', 'Video'))

    if input_type == 'Image':
        # Image Input
        image_input = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])

        # Question about the image
        question = st.text_input("(Optional) Enter a question about the image:")

        if st.button("Submit"):
            with col2:
                if image_input:
                    # Display image_put as PIL image
                    image_input = Image.open(image_input)
                    st.image(image_input)

                    # Get the caption
                    if question:
                        caption = lms.image_questioning(image_input, question)
                    else:
                        caption = lms.image_captioning(image_input)
                    st.success(caption)
                else:
                    st.warning("Please upload an image.")
    else:
        # Video Input
        video_input = st.file_uploader("Upload a video:", type=["mp4"])

        # Question about the video
        question = st.text_input("(Optional) Enter a question about the video:")

        if st.button("Submit"):
            with col2:
                if video_input:
                    st.video(video_input.getvalue())
                    vid = video_input.name
                    with open(vid, mode='wb') as f:
                        f.write(video_input.read()) # save video to disk

                    

                    if question:
                        answers = get_answers_every_n_seconds(vid, question, 5)
                        # Get the caption
                        summary = lms.video_questioning(answers, question)
                    else:
                        captions = get_captions_every_n_seconds(vid, 5)
                        # Get the caption
                        summary = lms.video_captioning(captions)
                    st.success(summary)
                else:
                    st.warning("Please upload a video.")

