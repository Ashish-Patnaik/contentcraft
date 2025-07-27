document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generate-btn');
    const loader = document.getElementById('loader');
    const outputSection = document.getElementById('output-section');
    const generatedContent = document.getElementById('generated-content');
    const copyBtn = document.getElementById('copy-btn');

    generateBtn.addEventListener('click', async () => {
        // 1. Get user inputs
        const url = document.getElementById('youtube-url').value;
        const tone = document.getElementById('tone-select').value;
        const formatType = document.getElementById('format-select').value;

        // 2. Basic validation
        if (!url) {
            alert('Please enter a YouTube URL.');
            return;
        }

        // 3. Show loader and hide previous results
        loader.style.display = 'block';
        outputSection.style.display = 'none';
        generateBtn.disabled = true;
        generateBtn.textContent = 'Generating...';

        try {
            // 4. Send request to the backend API
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    url: url,
                    tone: tone,
                    formatType: formatType
                }),
            });

            const data = await response.json();

            if (!response.ok) {
                // Handle errors from the backend (e.g., invalid URL, transcript disabled)
                throw new Error(data.error || 'An unknown error occurred.');
            }

            // 5. Display the result
            generatedContent.value = data.content;
            outputSection.style.display = 'block';

        } catch (error) {
            alert(`An error occurred: ${error.message}`);
        } finally {
            // 6. Hide loader and re-enable button
            loader.style.display = 'none';
            generateBtn.disabled = false;
            generateBtn.textContent = 'Generate Content';
        }
    });

    // Copy button functionality
    copyBtn.addEventListener('click', () => {
        generatedContent.select();
        try {
            document.execCommand('copy');
            // Temporarily change button icon to checkmark
            const icon = copyBtn.querySelector('i');
            icon.classList.remove('fa-copy');
            icon.classList.add('fa-check');
            setTimeout(() => {
                icon.classList.remove('fa-check');
                icon.classList.add('fa-copy');
            }, 2000);
        } catch (err) {
            alert('Failed to copy content: ' + err);
        }
    });
});