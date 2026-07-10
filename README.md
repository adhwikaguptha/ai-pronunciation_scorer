AI Pronunciation Analyzer
Overview

AI Pronunciation Analyzer is a full-stack web application that evaluates a user's English pronunciation by comparing a spoken audio recording with a reference text. The application transcribes speech using Faster-Whisper, analyzes pronunciation accuracy at the word level, identifies pronunciation issues, and generates personalized feedback.

Features
Upload English audio clips (30–45 seconds)
Compare speech against a reference text
AI-powered speech transcription using Faster-Whisper
Word-level pronunciation analysis
Pronunciation score and accuracy calculation
Detection of:
Mispronounced words
Missing words
Extra words
Unclear words
Personalized pronunciation feedback
Language detection
Temporary file handling with automatic deletion for privacy
Tech Stack
Frontend
React
Vite
Axios
CSS
Backend
FastAPI
Faster-Whisper
Pydub
FFmpeg
RapidFuzz
Python

Supported Audio Formats
WAV
MP3
M4A
OGG
OGA
OPUS
FLAC
WEBM
Project Structure
ai-pronounce/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   ├── config.py
│   │   └── main.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── .env.example
│
└── README.md
Local Installation
Clone the repository
git clone https://github.com/adhwikaguptha/ai-pronunciation_scorer.git
Backend
cd backend

python -m venv venv

Windows

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Create a .env file using .env.example

Run the backend

uvicorn app.main:app --reload

Backend URL

http://127.0.0.1:8000
Frontend
cd frontend

npm install

Create a .env file from .env.example

VITE_API_URL=http://127.0.0.1:8000/api

Run

npm run dev

Frontend

http://localhost:5173
Deployment
Frontend

Deployed on Vercel

Backend

Deployed on Render

Privacy
Audio files are temporarily stored during processing.
Uploaded files are automatically deleted after analysis.
No user audio is permanently stored.
No personal information such as name, email, or phone number is collected.
Future Improvements
Real-time progress updates
Phoneme-level pronunciation assessment
GPU acceleration
Background task processing
User authentication
Analysis history
Docker deployment
CI/CD pipeline
Enhanced pronunciation visualization
Author

Adhwika Guptha

B.Tech Artificial Intelligence & Machine Learning
