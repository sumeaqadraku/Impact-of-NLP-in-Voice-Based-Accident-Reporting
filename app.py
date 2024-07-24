from flask import Flask, request, send_from_directory, jsonify
import os

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
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], 'combined_audio.webm')
    audio_file.save(audio_path)

    # Placeholder response as transcription is removed
    return jsonify({'message': 'Audio file received', 'file': audio_path}), 200

if __name__ == '__main__':
    app.run(debug=True)
