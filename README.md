# Audio Noise Remover Web Application

A Flask-based web application that removes background noise from audio files using spectral gating techniques. Upload your audio file and download a cleaned version instantly.

## Features

- **Web-based Interface**: Simple and intuitive UI for uploading and processing audio files
- **Spectral Noise Reduction**: Advanced noise removal using Short-Time Fourier Transform (STFT)
- **Real-time Processing**: Fast audio processing with immediate download
- **Multiple Format Support**: Handles various audio formats supported by librosa
- **In-memory Processing**: Efficient handling of audio data without temporary file storage

## Demo

Upload an audio file → Process with noise reduction → Download cleaned audio

## How It Works

The application uses spectral gating to remove noise:

1. **Noise Profile Estimation**: Analyzes the first 0.5 seconds of audio to estimate the noise floor
2. **Spectral Analysis**: Converts audio to frequency domain using STFT
3. **Mask Generation**: Creates a binary mask to separate signal from noise
4. **Median Filtering**: Smooths the mask to reduce musical noise artifacts
5. **Signal Reconstruction**: Applies the mask and converts back to time domain using inverse STFT

## Project Structure

```
NOISE_REMOVER_APP/
│
├── __pycache__/                 # Python cache files
│   └── noise_remover.cpython-311.pyc
│
├── static/                      # Static assets
│   ├── script.js               # Frontend JavaScript logic
│   └── style.css               # Application styling
│
├── templates/                   # HTML templates
│   └── index.html              # Main application page
│
├── app.py                      # Flask application and routes
├── noise_remover.py            # Core noise removal algorithm
└── requirements.txt            # Python dependencies
```

## Technologies Used

### Backend
- **Flask**: Lightweight web framework for handling HTTP requests and routing
- **NumPy**: Numerical computing for array operations and audio manipulation
- **Librosa**: Audio analysis and feature extraction library
- **SciPy**: Signal processing utilities (median filtering)
- **SoundFile**: Audio file I/O operations

### Frontend
- **HTML5**: Structure and file upload interface
- **CSS3**: Styling and responsive design
- **JavaScript**: Client-side interactivity and form handling
### Setup

1. Clone the repository:
```bash
git clone https://github.com/abhinavkumar346/noise-remover-app.git
cd noise-remover-app
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
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

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Upload an audio file using the web interface

4. Click "Process" to remove noise

5. Download the cleaned audio file

## Dependencies

Create a `requirements.txt` file with:

```
Flask>=2.3.0
numpy>=1.24.0
librosa>=0.10.0
soundfile>=0.12.0
scipy>=1.10.0
```

## Algorithm Details

### Noise Removal Method

The application implements a spectral subtraction approach:

- **STFT Parameters**: Uses librosa's default window and hop length
- **Noise Estimation**: Averages the magnitude spectrum over the first 0.5 seconds
- **Masking**: Binary mask with median filtering (kernel size: 1×5)
- **Output Format**: WAV file at original sample rate

### Key Functions

#### `remove_noise_from_file(file_storage)`
Core noise removal function that:
- Accepts file-like objects from Flask requests
- Performs STFT-based noise reduction
- Returns an in-memory BytesIO buffer containing the cleaned audio

## Limitations

- Assumes noise is stationary and present in the first 0.5 seconds
- Works best for recordings with consistent background noise
- May introduce artifacts for very short audio files
- Musical noise can occur with highly variable signals

## Future Enhancements

- [ ] Support for multiple noise reduction algorithms
- [ ] Adjustable noise reduction strength
- [ ] Real-time audio preview
- [ ] Batch processing for multiple files
- [ ] Support for more output formats
- [ ] Advanced noise profiling options

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Troubleshooting

**Issue**: Application won't start
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check that port 5000 is available

**Issue**: Audio processing fails
- Verify the audio file is in a supported format
- Check file isn't corrupted
- Ensure file size is reasonable (< 100MB recommended)

**Issue**: Poor noise removal quality
- Try audio with clear noise in the first 0.5 seconds
- Consider pre-processing audio to ensure noise sample is representative
