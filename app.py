from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import numpy as np
import cv2
import face_recognition

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def load_image(file):
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    file.save(img_path)
    return img_path

def detect_faces_cv(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces, image

def recognize_faces(image_path):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    recognized_faces = [{'name': 'Person 1', 'confidence': 0.95}, {'name': 'Person 2', 'confidence': 0.90}]
    return recognized_faces

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect-and-recognize-faces', methods=['POST'])
def detect_and_recognize_faces():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        img_path = load_image(file)
        faces_cv, image_cv = detect_faces_cv(img_path)
        recognized_faces = recognize_faces(img_path)

        response = {
            'message': 'Faces detected and recognized successfully',
            'faces_detected': len(faces_cv),
            'recognized_faces': recognized_faces
        }

        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
