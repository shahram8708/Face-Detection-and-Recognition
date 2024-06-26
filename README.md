# Face Detection and Recognition

This project demonstrates face detection and recognition using Python, Flask, and OpenCV. It provides a web interface where users can upload images to detect faces and optionally perform recognition tasks.

## Features

- **Face Detection**: Upload an image to detect faces using OpenCV's Haar Cascade Classifier.
- **Face Recognition (Optional)**: Extend the application with face recognition capabilities using deep learning models.
- **Web Interface**: Simple and intuitive web interface powered by Flask for easy interaction.

## Prerequisites

- Python 3.6+
- Virtual environment tool (e.g., `venv`, `virtualenv`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shahram8708/face-detection-recognition.git
   cd face-detection-recognition
   ```

2. Create a virtual environment:

   ```bash
   # Using venv
   python -m venv venv
   # Activate the virtual environment (Windows)
   venv\Scripts\activate
   # Activate the virtual environment (Linux/Mac)
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://localhost:5000`.

3. Upload an image using the "Upload Image" button.

4. Click on "Detect Faces" to initiate face detection on the uploaded image.

5. Optionally, integrate face recognition by extending the backend (`app.py`) with appropriate recognition logic.

## File Structure

```
face-detection-recognition/
│
├── app.py           # Flask application setup and routes
├── static/
│   ├── css/
│   │   └── styles.css   # CSS styles for the web interface
│   └── js/
│       └── script.js    # JavaScript for client-side interaction
├── templates/
│   └── index.html    # HTML template for the web interface
├── README.md         # Project documentation
└── requirements.txt  # Python dependencies
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenCV](https://opencv.org/) - Open Source Computer Vision Library
- [Flask](https://flask.palletsprojects.com/) - Python Web Framework
- [Bootstrap](https://getbootstrap.com/) - Front-end Component Library

## Author

- Shah Ram
- GitHub: [Shah Ram](https://github.com/shahram8708)
