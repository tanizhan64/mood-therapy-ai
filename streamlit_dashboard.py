import streamlit as st
import pandas as pd
import altair as alt
import os

st.set_page_config(page_title="Mood Tracker Dashboard", layout="wide")
st.title("📊 Mood Tracker Dashboard")
st.markdown("Monitor how your emotions change over time.")

log_file = "data/mood_log.csv"

# 📊 Load the mood log CSV
if os.path.exists(log_file):
    df = pd.read_csv(log_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date

    st.subheader("📈 Mood Frequency Over Time")
    mood_counts = df.groupby(['date', 'emotion']).size().reset_index(name='count')

    chart = alt.Chart(mood_counts).mark_bar().encode(
        x='date:T',
        y='count:Q',
        color='emotion:N',
        tooltip=['date:T', 'emotion:N', 'count:Q']
    ).properties(width=800, height=400)

    st.altair_chart(chart, use_container_width=True)

    st.subheader("📝 Recent Mood Entries")
    st.dataframe(df.sort_values(by="timestamp", ascending=False).tail(10))

else:
    st.warning("⚠️ No mood log data found. Use the Mood Therapy app to submit entries first.")
