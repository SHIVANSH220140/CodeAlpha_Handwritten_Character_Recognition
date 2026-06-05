import streamlit as st
import tensorflow as tf
import numpy as np

from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.title("Handwritten Character Recognition")

model = tf.saved_model.load("../models/emnist_savedmodel")
infer = model.signatures["serving_default"]

canvas_result = st_canvas(
    fill_color="black",
    stroke_width=15,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

if st.button("Predict"):

    if canvas_result.image_data is not None:

        image = Image.fromarray(
            canvas_result.image_data.astype("uint8")
        )

        image = image.convert("L")

        image = image.resize((28, 28))

        image = np.array(image)

        image = image / 255.0

        image = image.reshape(1, 28, 28, 1).astype(np.float32)

        prediction = infer(tf.constant(image))

        probs = prediction["output_0"].numpy()

        predicted_class = np.argmax(probs)

        predicted_char = chr(predicted_class + 65)

        st.success(
            f"Predicted Character: {predicted_char}"
        )