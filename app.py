import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import random


st.title("MNIST Digit Generator")
st.markdown("""
**Display handwritten digits from the MNIST dataset.**  
Select a digit (0-9) and the app will show 5 random examples.
""")

#add digit to view
digit = st.slider("Select a digit:", 0, 9, 0)

@st.cache_data
def load_mnist_data():
    (x_train, y_train), (_, _) = tf.keras.datasets.mnist.load_data()
    #normalize images to [0, 1] range
    x_train = x_train / 255.0
    return x_train, y_train

#gen image
if st.button("Show Images"):
    x_train, y_train = load_mnist_data()

    st.subheader(f"Showing examples for digit: {digit}")
    
    digit_indices = np.where(y_train == digit)[0]

    random_indices = np.random.choice(digit_indices, 5, replace=False)
    
    #get the 5 images
    images = x_train[random_indices]
    
    cols = st.columns(5)
    for i, img in enumerate(images):
        with cols[i]:
            plt.figure(figsize=(2, 2))
            plt.imshow(img, cmap='gray', interpolation='nearest')
            plt.axis('off')
            st.pyplot(plt.gcf(), use_container_width=True)
            plt.clf()
