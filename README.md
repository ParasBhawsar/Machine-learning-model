# Machine Learning Model Prediction Web Application
This repository contains code for a Flask web application that allows users to upload images and make predictions using a pre-trained machine learning model. The model is trained to classify images into four classes: "Leaf Blight", "Leaf Fall Autumn", "Caterpillar", and "Healthy Leaf".

![Alt text](https://github.com/ParasBhawsar/New-folder--2-/blob/main/predict.jpeg)

Upload an image using the provided form and click "Predict" to see the predicted class.

# Files
-flask_app.py: Flask application file containing the backend code for image preprocessing, model loading, prediction, and routing.
-index.html: HTML template file for the frontend interface.
-bg.jpg: Background image used in the HTML template.
-Zambul.h5: Pre-trained TensorFlow/Keras model file.
requirements.txt: List of Python dependencies.
-HTML Template
The index.html file provides the user interface for the web application. Users can upload an image, and upon submission, the predicted class is displayed.

# Model
The pre-trained model (Zambul.h5) is loaded using TensorFlow/Keras. It is capable of classifying images into one of the four specified classes.

# Additional Information
The Flask application runs in debug mode (debug=True) for development purposes. Change this to debug=False for production deployment.
Make sure to replace the placeholder class names and adjust them according to the actual classes your model is trained on.
The application uses CSS for styling. You can modify the CSS styles in the <style> section of the HTML template (index.html).
Ensure that the background image (bg.jpg) is placed in the correct directory or update the path accordingly in the CSS.

# Note
This application serves as a simple example of deploying a machine learning model using Flask. Make sure to adapt it to your specific requirements and environment.

Feel free to contribute, report issues, or suggest improvements.

For any questions or inquiries, please contact [bhawsarparas@gmail.com].

Enjoy predicting with your machine learning model! 🚀
