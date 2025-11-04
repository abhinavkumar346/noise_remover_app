document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Stop the form from submitting normally

    const form = event.target;
    const formData = new FormData(form);
    const statusDiv = document.getElementById('status');
    const downloadDiv = document.getElementById('download-link');
    const submitButton = document.getElementById('submit-button');

    // Reset UI
    statusDiv.textContent = 'Uploading and processing...';
    downloadDiv.innerHTML = '';
    submitButton.disabled = true;

    try {
        const response = await fetch('/process', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            // Get the file data as a "blob"
            const blob = await response.blob();
            
            // Create a temporary URL for the blob
            const url = window.URL.createObjectURL(blob);
            
            // Create a download link
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'cleaned_audio.wav'; // The filename for the download
            
            document.body.appendChild(a);
            a.click(); // Trigger the download
            
            // Clean up
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
            
            statusDiv.textContent = 'Success! Your file is downloading.';

        } else {
            // Handle server errors
            statusDiv.textContent = `Error: ${response.statusText}`;
        }

    } catch (error) {
        // Handle network errors
        console.error('Error:', error);
        statusDiv.textContent = 'An error occurred. Please try again.';
    } finally {
        submitButton.disabled = false; // Re-enable the button
    }
});