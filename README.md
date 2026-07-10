# AI Pronunciation Analyzer

An AI-powered web application that evaluates English pronunciation by comparing a user's spoken audio with a reference text. The application uses Faster-Whisper for speech recognition and performs word-level pronunciation analysis to generate scores and personalized feedback.

---

## Live Demo

**Frontend:** https://YOUR-VERCEL-URL.vercel.app

**Backend:** https://YOUR-RENDER-URL.onrender.com

---

## Features

- AI-powered English speech transcription
- Pronunciation scoring using word-level comparison
- Detects:
  - Mispronounced words
  - Missing words
  - Extra words
  - Unclear words
- Personalized pronunciation feedback
- Language detection
- Audio duration validation (30–45 seconds)
- Multiple audio format support
- Automatic deletion of uploaded audio after analysis

---

## Tech Stack

### Frontend

- React
- Vite
- Axios
- CSS

### Backend

- FastAPI
- Faster-Whisper
- Pydub
- FFmpeg
- RapidFuzz
- Python

### Deployment

- Vercel (Frontend)
- Render (Backend)

---

# System Architecture

```text
                    User
                      │
                      ▼
            React (Vite Frontend)
                      │
         Upload Audio + Reference Text
                      │
                 REST API (HTTP)
                      │
                      ▼
             FastAPI Backend
                      │
     ┌────────────────┼────────────────┐
     │                │                │
     ▼                ▼                ▼
Audio Service   Whisper Service  Scoring Service
     │                │                │
Validate Audio   Speech-to-Text   Word Comparison
Convert to WAV  Faster-Whisper    Score Generation
     │                │                │
     └────────────────┼────────────────┘
                      │
                      ▼
             Feedback Service
                      │
                      ▼
                JSON Response
                      │
                      ▼
              React Frontend
```

---

# Project Workflow

1. User enters the reference text.
2. User uploads an English audio clip (30–45 seconds).
3. Backend validates the file and audio duration.
4. Audio is converted to WAV format.
5. Faster-Whisper transcribes the speech.
6. Transcript is compared with the reference text.
7. Pronunciation score is calculated.
8. Personalized feedback is generated.
9. Results are displayed in the frontend.
10. Temporary audio files are automatically deleted.

---

## Supported Audio Formats

- WAV
- MP3
- M4A
- OGG
- OGA
- OPUS
- FLAC
- WEBM

---

## Project Structure

```text
ai-pronounce/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   │   ├── audio_service.py
│   │   │   ├── whisper_service.py
│   │   │   ├── scoring_service.py
│   │   │   ├── feedback_service.py
│   │   │   └── pronunciation_service.py
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
│   ├── package.json
│   └── .env.example
│
└── README.md
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/adhwikaguptha/ai-pronunciation_scorer.git
```

---

## Backend Setup

```bash
cd backend

python -m venv venv
```

### Activate Virtual Environment

Windows CMD

```bash
venv\Scripts\activate
```

Git Bash

```bash
source venv/Scripts/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file using `.env.example`.

Run the backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

```bash
cd frontend

npm install
```

Create a `.env` file from `.env.example`

```env
VITE_API_URL=http://127.0.0.1:8000/api
```

Run the frontend

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# API Endpoint

### Analyze Pronunciation

```
POST /api/analyze
```

### Request

- Audio File
- Reference Text

### Response

```json
{
  "score": 92.4,
  "accuracy": 95.3,
  "language": "en",
  "transcript": "...",
  "analysis": [],
  "feedback": []
}
```

---

# Pronunciation Scoring

The application compares the transcribed speech with the reference text using word-level alignment.

### Accuracy

Average similarity score of all matched words.

### Completeness

Percentage of reference words successfully spoken.

### Final Score

```
Final Score =
(0.70 × Accuracy)
+
(0.30 × Completeness)
```

The application highlights:

- Mispronounced words
- Missing words
- Extra words
- Unclear words

Correctly spoken words are intentionally excluded from the detailed analysis to keep feedback concise and actionable.

---

# Privacy

The application follows a privacy-first approach.

- Audio files are stored only temporarily during processing.
- Uploaded audio is automatically deleted after analysis.
- No permanent storage of user recordings.
- No personal information such as name, email, or phone number is collected.
- Reference text is processed only for generating pronunciation analysis.

---

# Future Improvements

- Real-time progress updates using WebSockets
- Phoneme-level pronunciation assessment
- GPU-based Faster-Whisper inference
- User authentication
- Pronunciation history dashboard
- Docker deployment
- CI/CD pipeline
- Improved visualization with pronunciation timelines

---

# Author

**Adhwika Guptha**

B.Tech – Artificial Intelligence & Machine Learning

GitHub: https://github.com/adhwikaguptha
