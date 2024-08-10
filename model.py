import numpy as np
import tensorflow as tf
from PIL import Image
import streamlit as st
import logging

logging.basicConfig(level=logging.INFO)

# Fungsi untuk memuat model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('Model_VGG16.h5')
    return model

# Fungsi untuk memprediksi gambar
def predict_image(model, image):
    # Konversi gambar ke format RGB jika tidak dalam format tersebut
    if image.mode != 'RGB':
        logging.info(f"Converting image from {image.mode} to RGB")
        image = image.convert('RGB')
        
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    logging.info(f"Input image shape: {image.shape}")  # Debugging shape of the input image
    predictions = model.predict(image)
    return np.argmax(predictions, axis=1)[0]


