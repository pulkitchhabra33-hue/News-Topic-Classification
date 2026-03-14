import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.models import load_model
import numpy as np
import pickle

model= tf.keras.models.load_model("news_classifier.h5", compile= False, safe_mode= False)

tokenizer= pickle.load(open("tokenizer.pkl", "rb"))
max_length= 200

st.title("News Topic Classifier")

text= st.text_area("Enter news headline")

if st.button("Predict"):
    seq= tokenizer.texts_to_sequences([text])
    padded= pad_sequences(seq, maxlen= max_length, padding= "post", truncating= "post")

    pred= model.predict(padded)

    classes= ["World", "Sports", "Business", "Sci/Tech"]

    st.success(classes[np.argmax(pred)])