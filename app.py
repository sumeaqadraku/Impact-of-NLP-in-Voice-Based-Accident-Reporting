from flask import Flask, request, send_from_directory, jsonify
import os
import numpy as np
import librosa
from hmmlearn import hmm
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'recorded_audio.webm')
    audio_file.save(file_path)

    # Process the audio file
    try:
        audio_data, sr = librosa.load(file_path, sr=None)  # Load audio file with original sampling rate
        features = extract_features(audio_data, sr)
        result = run_hmm_model(features)
        return jsonify({'text': result, 'file': file_path}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def extract_features(audio_data, sr):
    # Extract MFCC features from the audio data
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sr, n_mfcc=13)
    return mfccs.T  # Transpose for HMM compatibility

def run_hmm_model(features):
    # Define and fit the HMM model (Example with GMM-HMM)
    model = hmm.GaussianHMM(n_components=5, covariance_type='diag', n_iter=1000)
    model.fit(features)
    # Predict or use the model as needed (Example prediction)
    return "Recognized Text Placeholder"  # Replace with actual model prediction

if __name__ == '__main__':
    app.run(debug=True)
