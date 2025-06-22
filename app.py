import streamlit as st
import numpy as np
import random
import tensorflow as tf
import matplotlib.pyplot as plt


st.title("MNIST Digit Generator")
st.markdown("""
**Generate synthetic handwritten digits** similar to the MNIST dataset.  
Select a digit (0-9) and the app will create 5 variations.
""")


digit = st.slider("Select a digit:", 0, 9, 0)

#mnist data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


def generate_digit_image(digit):
    img = np.zeros((28, 28))
    
    img += np.random.rand(28, 28) * 0.3
    
    patterns = {
        0: [(7,7), (7,20), (20,20), (20,7), (7,7)],
        1: [(10,5), (10,22)],
        2: [(7,20), (20,20), (20,15), (7,7), (20,7)],
        3: [(7,20), (20,20), (7,13), (20,13), (7,7)],
        4: [(7,20), (7,13), (20,13), (20,20), (20,7)],
        5: [(20,20), (7,20), (7,13), (20,13), (20,7), (7,7)],
        6: [(20,20), (7,20), (7,7), (20,7), (20,13), (7,13)],
        7: [(7,20), (20,20), (10,7)],
        8: [(7,13), (7,20), (20,20), (20,13), (7,13), (7,7), (20,7)],
        9: [(20,13), (7,13), (7,20), (20,20), (20,7)]
    }
    
    # Draw the digit pattern with random variations
    for i in range(len(patterns[digit]) - 1):
        start = patterns[digit][i]
        end = patterns[digit][i+1]
        
        # Add slight random offsets to positions
        offset_x = random.randint(-1, 1)
        offset_y = random.randint(-1, 1)
        
        # Draw line between points
        x = np.linspace(start[0]+offset_x, end[0]+offset_x, 10)
        y = np.linspace(start[1]+offset_y, end[1]+offset_y, 10)
        
        for px, py in zip(x, y):
            if 0 <= int(px) < 28 and 0 <= int(py) < 28:
                img[int(px), int(py)] = 0.8  # Digit color
    
    # Add random noise to digit pixels
    digit_mask = img > 0.5
    img[digit_mask] += np.random.rand(*img[digit_mask].shape) * 0.5
    
    # Normalize and clip values
    img = np.clip(img, 0, 1)
    return img

# Generate and display images
if st.button("Generate Images"):
    st.subheader(f"Generated Digit: {digit}")
    
    # Create 5 images
    images = [generate_digit_image(digit) for _ in range(5)]
    
    # Display in a grid
    cols = st.columns(5)
    for i, img in enumerate(images):
        with cols[i]:
            plt.figure(figsize=(2, 2))
            plt.imshow(img, cmap='gray', interpolation='nearest')
            plt.axis('off')
            st.pyplot(plt.gcf(), use_container_width=True)
            plt.clf()

image_index = 0
image = x_train[image_index]
label = y_train[image_index]

# Print the label of the image
st.write(f"The label for this image is: {label}")

# Display the image
plt.imshow(image, cmap='gray')
plt.title(f"Label: {label}")
plt.axis('off')  # Hide the axes for a cleaner look
plt.show()
