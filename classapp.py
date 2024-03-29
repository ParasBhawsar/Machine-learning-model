from flask import Flask, render_template, request
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('Zambul.h5')

# Define the class names (replace with your actual class names)
#class_names = ["caterpillar", "Healthy_leaf", "Leaf Blight","Leaf Fall Autumn"]  # Add your class names here
class_names = ["Leaf Blight", "Leaf Fall Autumn", "caterpillar","Healthy_leaf"] 
#healthy ->cater
#cater->leaf fall autum
#leaf fall autum ->leaf bright
app = Flask(__name__)

# Define function to preprocess the image
def preprocess_image(img):
    width, height = 64, 64  # Specify the dimensions you used for training
    img = cv2.resize(img, (width, height))
    img = np.expand_dims(img, axis=0) / 255.0
    return img

# Define function to perform prediction
def predict_image(img):
    img = preprocess_image(img)
    prediction = model.predict(img)
    predicted_class_index = np.argmax(prediction)
    predicted_class_name = class_names[predicted_class_index-1]
    return predicted_class_name

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_class_name = None
    if request.method == 'POST':
        # Get the image file from the request
        file = request.files['file']
        # Read the image file
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        # Perform prediction
        predicted_class_name = predict_image(img)
    return render_template('index.html', predicted_class_name=predicted_class_name)

if __name__ == "__main__":
    app.run(debug=True)
