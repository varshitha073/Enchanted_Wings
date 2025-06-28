from flask import Flask, render_template, request, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
import os

app = Flask(__name__)

# Folder where sample butterfly images are stored
SAMPLE_FOLDER = 'sample_images'

# Load the pre-trained VGG16 model
model = load_model('vgg16_model.h5')

# Replace with all 75 class names (ensure order matches model training)
class_names = ['Peacock Pansy', 'Common Crow', 'Monarch', 'Painted Lady', 'Swallowtail']

@app.route('/')
def index():
    # List available sample images
    image_files = [f for f in os.listdir(SAMPLE_FOLDER) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    return render_template('index.html', images=image_files)

@app.route('/predict', methods=['POST'])
def predict():
    filename = request.form.get('selected_image')
    if not filename:
        return "No image selected", 400

    filepath = os.path.join(SAMPLE_FOLDER, filename)
    if not os.path.exists(filepath):
        return f"Image not found: {filepath}", 404

    # Load and preprocess the image
    img = load_img(filepath, target_size=(224, 224))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Predict using model
    preds = model.predict(x)
    pred_class = class_names[np.argmax(preds)]

    # Only send prediction (not image filename)
    return render_template('result.html', prediction=pred_class)

# Optional: Keep this route if you use images elsewhere
@app.route('/sample_images/<filename>')
def serve_image(filename):
    return send_from_directory(SAMPLE_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
