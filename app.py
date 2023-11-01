# Import library
from tensorflow.keras.models import load_model
import streamlit as st
from PIL import ImageOps, Image
import numpy as np

# Name page title
st.set_page_config(page_title="Rock Paper Scissors", layout="wide")
st.title("Rock Paper Scissors Hand Pose Detection")
try:
    # Input image
    file = st.file_uploader(
        "Upload your hand with rock, paper, or scissors pose!", type=["png", "jpg"]
    )
    image = Image.open(file)
    img = ImageOps.fit(image, (224, 224))
    # Grayscale the image
    gray = ImageOps.grayscale(img)

    img_array = np.asarray(gray)
    x = np.expand_dims(img_array, axis=0)
    images = np.vstack([x])

    # get model
    model_path = "model-20-0.9909.hdf5"
    model = load_model(model_path)

    # Predict uploaded image with model
    classes = model.predict(images)

    if classes[0][0] == 1:
        st.info("It's Paper!")
    elif classes[0][1] == 1:
        st.info("It's Rock!")
    else:
        st.info("It's Scissors!")
    left_co, cent_co, last_co = st.columns(3)
    with cent_co:
        st.image(file)

except:
    # Set error if image isn't uploded yet
    st.error("Please upload your hand!")
    st.stop()
