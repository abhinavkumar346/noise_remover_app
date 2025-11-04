from flask import Flask, request, send_file, render_template, make_response
from noise_remover import remove_noise_from_file
import io

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_audio():
    """
    Handles the audio file upload, processes it, 
    and sends back the cleaned file.
    """
    if 'audio_file' not in request.files:
        return "No file part", 400

    file = request.files['audio_file']

    if file.filename == '':
        return "No selected file", 400

    if file:
        # Process the file using your refactored function
        cleaned_buffer = remove_noise_from_file(file)
        
        if cleaned_buffer:
            # Send the in-memory buffer back as a file download
            return send_file(
                cleaned_buffer,
                mimetype='audio/wav',
                as_attachment=True,
                download_name='cleaned_audio.wav'
            )
        else:
            return "Error processing file", 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)