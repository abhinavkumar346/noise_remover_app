import numpy as np
import librosa
import soundfile as sf
from scipy.signal import medfilt
import io

def remove_noise_from_file(file_storage):
    """
    Takes a file-like object (from Flask's request) and returns
    an in-memory WAV file (BytesIO buffer) of the cleaned audio.
    """
    try:
        # 1. Load audio from the in-memory file
        #    librosa.load can handle file-like objects
        y, sr = librosa.load(file_storage, sr=None)

        # 2. Perform your noise removal logic
        S_full, phase = librosa.magphase(librosa.stft(y))
        
        # Estimate noise: use first 0.5 seconds for more robust estimation
        noise_frames = int(sr * 0.5)
        if y.shape[0] < noise_frames:
             noise_frames = y.shape[0] # Handle very short files
             
        noise_power = np.mean(S_full[:, :noise_frames], axis=1)
        
        mask = S_full > noise_power[:, None]
        mask = mask.astype(float)
        mask = medfilt(mask, kernel_size=(1, 5))
        
        S_clean = S_full * mask
        y_clean = librosa.istft(S_clean * phase)

        # 3. Write the cleaned audio to an in-memory buffer
        output_buffer = io.BytesIO()
        sf.write(output_buffer, y_clean, sr, format='WAV')
        output_buffer.seek(0) # Rewind buffer to the beginning

        return output_buffer

    except Exception as e:
        print(f"Error processing audio: {e}")
        return None