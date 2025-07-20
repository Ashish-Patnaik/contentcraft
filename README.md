# 🚀 ContentCraft: AI YouTube Content Factory

Transform any public YouTube video into a complete suite of ready-to-publish social media content in seconds. ContentCraft harnesses the power of AI to automatically convert video transcripts into engaging Twitter threads, professional LinkedIn posts, eye-catching Instagram captions, and more.

![ContentCraft Banner](https://via.placeholder.com/800x400/1a1a1a/ffffff?text=ContentCraft+AI+YouTube+Content+Factory)

## ✨ Features

- **🎯 Multi-Platform Formatting**: Generate content perfectly styled for:
  - Twitter (Threads & Single Posts)
  - LinkedIn (Professional posts)
  - Instagram (Captions with hashtags)
  - Reddit (Community posts)
  - News Articles (Blog-ready format)

- **🎨 Tone Customization**: Set the perfect mood for your audience:
  - Engaging & Conversational
  - Controversial & Thought-provoking
  - Professional & Corporate
  - Humorous & Lighthearted
  - Educational & Informative

- **📝 Transcript-Powered**: Automatically fetches full transcripts from any public YouTube video
- **🤖 AI-Driven Generation**: Powered by Google Gemini Pro for high-quality, human-like content
- **✏️ Built-in Editor**: Clean interface to fine-tune AI output before publishing
- **🌙 Modern UI**: Dark-themed, responsive design optimized for user experience
- **☁️ Cloud-Ready**: Seamless deployment to hosting platforms like Render

## 🛠️ Tech Stack

**Frontend**
- HTML5, CSS3, JavaScript
- Responsive design with modern dark theme

**Backend**
- Python 3.8+
- Flask web framework
- Gunicorn production server

**Core Libraries**
- `google-generativeai` - Gemini API integration
- `youtube-transcript-api` - Video transcript extraction
- `python-dotenv` - Environment variable management

**Deployment**
- Render (recommended)
- GitHub integration

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have:
- Python 3.8 or newer installed
- A Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- Git installed on your machine

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/contentcraft.git
cd contentcraft
```

### 2. Set Up Virtual Environment

Create and activate a virtual environment to isolate project dependencies:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install all required packages from the requirements file:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and add your API key:

```bash
# Create the environment file
touch .env
```

Add the following to your `.env` file:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

> **⚠️ Important:** Never commit your `.env` file to version control. It's already included in `.gitignore` for security.

### 5. Run the Application

Start the Flask development server:

```bash
python app.py
```

You should see output similar to:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

Open your browser and navigate to `http://127.0.0.1:5000` to start using ContentCraft!

## 📖 How to Use

1. **Paste YouTube URL**: Copy any public YouTube video URL into the input field
2. **Select Platform**: Choose your target social media platform
3. **Pick a Tone**: Select the tone that matches your brand or audience
4. **Generate Content**: Click generate and let AI work its magic
5. **Edit & Refine**: Use the built-in editor to make final adjustments
6. **Copy & Publish**: Copy the formatted content and publish across your channels


## 🗂️ Project Structure

```
contentcraft/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment config
├── .env                  # Environment variables (not committed)
├── .gitignore           # Git ignore rules
├── static/
│   ├── css/
│   │   └── style.css    # Application styles
│   └── js/
│       └── script.js    # Frontend JavaScript
├── templates/
│   └── index.html       # Main application template
└── README.md           # This file
```

## 🛣️ Roadmap

- **🔗 Social Media Integration**: Direct posting to Twitter and LinkedIn APIs
- **🖼️ AI Image Generation**: Automatic relevant image suggestions for posts
- **👤 User Authentication**: Save generation history and personal preferences
- **⚡ Advanced Customization**: Custom @handles, names, and brand-specific content
- **📊 Analytics Dashboard**: Track content performance across platforms
- **🔄 Batch Processing**: Process multiple videos simultaneously

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) - Excellent transcript extraction library
- [Google Gemini API](https://ai.google.dev/) - Powerful AI language model
- [Flask](https://flask.palletsprojects.com/) - Lightweight and flexible web framework


## ⭐ Show Your Support

If you found ContentCraft helpful, please consider:

- ⭐ **[Star this repository](https://github.com/YOUR_USERNAME/contentcraft)** to show your support
- 🐦 **[Follow me on X (Twitter)](https://x.com/YOUR_TWITTER_HANDLE)** for updates and more AI tools
- 🔄 **Share this project** with others who might find it useful

[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/contentcraft?style=social)](https://github.com/YOUR_USERNAME/contentcraft/stargazers)
[![Twitter Follow](https://img.shields.io/twitter/follow/YOUR_TWITTER_HANDLE?style=social)](https://x.com/YOUR_TWITTER_HANDLE)

---

**Made with ❤️ by [Ashish Patnaik]**

*Transform your YouTube content into social media gold with ContentCraft!*
