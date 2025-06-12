import streamlit as st
import time
from utils.mood_classifier import detect_mood
from utils.calming_quotes import get_quote
import pandas as pd
from datetime import datetime
import os

# 🎵 Music playlist by mood
mood_music_links = {
    "joy": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",  # Happy pop
    "sadness": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",  # Calming piano
    "anger": "https://youtu.be/1ZYbU82GVz4?si=Yz3EYfxRQwfLvqlE",  # Peaceful nature sounds
    "fear": "https://youtu.be/b5BNUa_op2o?si=0QooEoGszHb-w3oe",  # Deep relaxation music
    "love": "https://youtu.be/kffacxfA7G4?si=5-sJO8JbKX2Vq97L",  # Love melody
    "surprise": "https://youtu.be/QkjFtDZz4Xs?si=cfEr1oOBUu0LDr0s"  # Light mood lo-fi
}


# 📦 Save mood log
def log_mood(text, mood, quote, music_link):
    os.makedirs("data", exist_ok=True)
    path = "data/mood_log.csv"
    df = pd.DataFrame([{
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input": text,
        "emotion": mood,
        "quote": quote,
        "music": music_link
    }])
    if os.path.exists(path):
        df.to_csv(path, mode='a', header=False, index=False)
    else:
        df.to_csv(path, index=False)

# 🌐 Streamlit UI
st.set_page_config(page_title="AI Mood Therapy", layout="centered")
st.title("🌈 AI Mood Therapy & Healing System")

user_input = st.text_input("🧠 How do you feel today?")

if st.button("🎯 Analyze My Mood"):
    if not user_input.strip():
        st.warning("Please enter a sentence or emotion.")
        st.stop()

    mood, score = detect_mood(user_input)
    quote = get_quote(mood)
    music_link = mood_music_links.get(mood, "https://www.youtube.com/watch?v=1ZYbU82GVz4")

    log_mood(user_input, mood, quote, music_link)

    st.success(f"🧠 Detected Mood: **{mood.capitalize()}** (Confidence: {score})")
    st.markdown(f"💬 *{quote}*")
    st.video(music_link)

# 🧘 Breathing Exercise
if st.button("🧘 Start Breathing Session"):
    st.subheader("✨ Calm Breathing: Inhale → Hold → Exhale")
    placeholder = st.empty()
    for i in range(3):
        placeholder.markdown("### 🌬️ Inhale…")
        time.sleep(4)
        placeholder.markdown("### ✋ Hold…")
        time.sleep(4)
        placeholder.markdown("### 😮‍💨 Exhale…")
        time.sleep(4)
    placeholder.markdown("✅ You're calm now. Breathe easy 🌸")
