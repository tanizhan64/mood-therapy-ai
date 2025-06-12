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

# 📝 Save mood entry to CSV
def log_mood(text, mood, quote, music_link):
    log_path = "data/mood_log.csv"
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame([{
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input": text,
        "emotion": mood,
        "quote": quote,
        "music": music_link
    }])
    if os.path.exists(log_path):
        df.to_csv(log_path, mode='a', header=False, index=False)
    else:
        df.to_csv(log_path, index=False)

# 🌐 Streamlit App UI
st.set_page_config(page_title="AI Mood Therapy", layout="centered")
st.title("🌈 AI Mood Therapy & Healing System")

user_input = st.text_input("🧠 How do you feel today?")

if st.button("🎯 Analyze My Mood"):
    if user_input:
        mood = detect_mood(user_input)
        quote = get_quote(mood)
        music_link = mood_music_links.get(mood, "https://www.youtube.com/watch?v=1ZYbU82GVz4")
        log_mood(user_input, mood, quote, music_link)

        st.success(f"🧠 Detected Mood: **{mood.capitalize()}**")
        st.markdown(f"💬 *{quote}*")
        st.markdown(f"[🎵 Click to Play Healing Music]({music_link})")

# 🧘‍♂️ Breathing Session
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
    placeholder.markdown("✅ Well done! You're calm and centered 🌸")
