import os
import re
from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-2.5-flash')
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    model = None

app = Flask(__name__)

def get_video_id(youtube_url):
    """Extracts the YouTube video ID from a URL."""
    # Regex to find video ID in various YouTube URL formats
    regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, youtube_url)
    if match:
        return match.group(1)
    return None

@app.route('/')
def index():
    """Renders the main page."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_content():
    """Handles the content generation request."""
    data = request.json
    url = data.get('url')
    tone = data.get('tone')
    format_type = data.get('formatType')

    if not url or not tone or not format_type:
        return jsonify({'error': 'Missing required fields'}), 400

    video_id = get_video_id(url)
    if not video_id:
        return jsonify({'error': 'Invalid YouTube URL'}), 400

    # 1. Get Transcript
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([item['text'] for item in transcript_list])
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return jsonify({'error': f"Could not retrieve transcript for this video. It might be disabled. Error: {e}"}), 500

    # 2. Pass to AI API (Gemini)
    if not model:
        return jsonify({'error': 'Gemini AI model is not configured. Check your API key.'}), 500
        
    # Construct a detailed prompt for better results
    prompt = f"""
    Based on the following YouTube video transcript, please create content for a {format_type}.
    The desired tone for the content is: {tone}.
    Your output should include only the content without any additional explanations or instructions or involvement of your.

    Your output should be ready to be published. 
    If you are creating a Twitter Thread, please number the tweets like "1/n", "2/n", etc.
    If you are creating an article, use markdown for formatting like headers and lists.
    For Instagram, include relevant emojis and hashtags.
    For a LinkedIn post, maintain a professional tone but make it engaging.

    Here is the transcript:
    ---
    {transcript}
    ---
    """

    try:
        response = model.generate_content(prompt)
        generated_text = response.text
        return jsonify({'content': generated_text})
    except Exception as e:
        print(f"Error generating content with Gemini: {e}")
        return jsonify({'error': f'Failed to generate content from AI. Error: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)