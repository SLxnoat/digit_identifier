import streamlit as st
from streamlit_drawable_canvas import st_canvas
import tensorflow as tf
from PIL import Image
import numpy as np

#Load trained model
model = tf.keras.models.load_model("models/mnist_cnn_model.keras")

st.title("MNIST Digit Classifier 🖌️")
st.write("Draw a digit (0-9) below and click Predict.")

#Create a drawing canvas
canvas_result = st_canvas(
    fill_color="#000000",  #bg color
    stroke_width=15,
    stroke_color="#FFFFFF",  # Draw in white
    background_color="#000000",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas"
)

if st.button("Predict"):
    if canvas_result.image_data is not None:
        #Convert to grayscale, resize to 28x28
        img = Image.fromarray(np.uint8(canvas_result.image_data[:,:,0])).convert('L')
        img = img.resize((28,28))
        img_array = np.array(img).reshape(1,28,28,1)/255.0

        #Make prediction
        prediction = model.predict(img_array)
        st.write(f"Predicted Digit: {np.argmax(prediction)}")
