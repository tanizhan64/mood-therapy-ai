import streamlit as st
import time
import os
import pandas as pd
from datetime import datetime

# Fix for relative imports when running from root
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

from utils.mood_classifier import detect_mood
from utils.calming_quotes import get_quote

# 🎵 Mood-based music links
mood_music_links = {
    "joy": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
    "sadness": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "anger": "https://www.youtube.com/watch?v=lTRiuFIWV54",
    "fear": "https://www.youtube.com/watch?v=b49UInx0mNw",
    "love": "https://www.youtube.com/watch?v=450p7goxZqg",
    "surprise": "https://www.youtube.com/watch?v=cBNqZKWj5e8"
}

# 📝 Mood log saver
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
        st.warning("Please enter a message or sentence to analyze.")
        st.stop()

    mood, score = detect_mood(user_input)
    quote = get_quote(mood)
    music_link = mood_music_links.get(mood, "https://www.youtube.com/watch?v=1ZYbU82GVz4")

    log_mood(user_input, mood, quote, music_link)

    st.success(f"🧠 Detected Mood: **{mood.capitalize()}** (Confidence: {score})")
    st.markdown(f"💬 *{quote}*")
    st.video(music_link)

# 🧘 Breathing session
if st.button("🧘 Start Breathing Session"):
    st.subheader("✨ Breathing Cycle: Inhale → Hold → Exhale")
    placeholder = st.empty()
    for _ in range(3):
        placeholder.markdown("### 🌬️ Inhale…")
        time.sleep(4)
        placeholder.markdown("### ✋ Hold…")
        time.sleep(4)
        placeholder.markdown("### 😮‍💨 Exhale…")
        time.sleep(4)
    placeholder.markdown("✅ You're calm. Stay peaceful 🌸")
