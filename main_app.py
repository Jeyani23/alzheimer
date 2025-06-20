import streamlit as st
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os
from datetime import datetime
from report_generator import generate_pdf_report
from email_sender import send_email
from chatbot import get_response

import gdown
import os
from keras.models import load_model

# Define model path
model_path = "model/alzheimer.h5"

# Download if not already downloaded
if not os.path.exists(model_path):
    os.makedirs("model", exist_ok=True)
    gdown.download("https://drive.google.com/file/d/1EHeTTFKg353joSyQfOuCnmLkonoKpsSs/view?usp=sharing", model_path, quiet=False)

# Load the model
model = load_model(model_path)

class_names = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']

st.set_page_config(page_title="AlzheimerAI Report Generator", layout="wide")
st.title("🧠 AlzheimerAI: MRI Classification and Report Generator")

st.sidebar.header("Patient Information")
name = st.sidebar.text_input("Patient Name")
age = st.sidebar.text_input("Age")
email = st.sidebar.text_input("Email ID")

uploaded_file = st.file_uploader("Upload MRI Image", type=["jpg", "png", "jpeg"])

if uploaded_file and name and age and email:
    img = image.load_img(uploaded_file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.

    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    result = class_names[class_index]
    confidence = round(float(np.max(prediction)) * 100, 2)

    st.image(img, caption=f"Uploaded MRI Scan", use_column_width=True)
    st.success(f"Prediction: **{result}** with **{confidence}%** confidence")

    report_filename = generate_pdf_report(name, age, result, confidence)
    with open(report_filename, "rb") as file:
        st.download_button("📄 Download Report", file, file_name=os.path.basename(report_filename))

    if st.button("📧 Send Report to Email"):
        send_email(email, name, report_filename)
        st.success("Report sent successfully!")

st.subheader("💬 AlzheimerAI Assistant")
user_input = st.text_input("Ask me anything about Alzheimer’s:")
if user_input:
    response = get_response(user_input)
    st.write(f"🤖 {response}")
