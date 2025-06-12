# AI Mood Therapy & Healing

> A personalized, calming AI companion that detects your mood and delivers healing quotes, emotion-matched music, breathing exercises, and an emotional health dashboard — built for everyone.

---

## 🧠 Features

- 🎯 **Mood Detection**: Uses NLP (Hugging Face Transformers) to detect user emotion from text
- 💬 **Calming Quote Generator**: Personalized motivational quote based on your emotion
- 🎵 **Music Recommender**: YouTube/Spotify links for emotion-matched music therapy
- 🧘‍♂️ **Guided Breathing UI**: Visual 4-4-4 breathing cycle to reduce stress
- 📊 **Mood Tracker**: Stores daily entries and visualizes emotion trends over time
- 🧾 **CSV Logging**: All mood sessions are saved for emotional history tracking

---

## 🛠️ Tech Stack

- Python · Streamlit · Gradio · Hugging Face Transformers  
- Pandas · Altair · YouTube Links · Optional: MusicGen, DALL·E, GPT-4

---

## 📁 Folder Structure

mood-therapy-ai/
├── app/
│ ├── streamlit_app.py # Full interactive app
│ └── streamlit_dashboard.py # Mood tracking visualization
├── data/
│ └── mood_log.csv # Stored mood sessions
├── assets/
│ └── calm_music.mp3 # Background music (optional)
├── utils/
│ ├── mood_classifier.py # Emotion detection pipeline
│ └── calming_quotes.json # Quotes by mood
├── requirements.txt
└── README.md
