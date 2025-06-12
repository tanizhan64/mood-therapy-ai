# streamlit_dashboard.py
import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(page_title="Mood Tracker", layout="wide")

st.title("📊 Mood Tracker Dashboard – AI Healing Companion")

# Load the log
log_file = "data/mood_log.csv"
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
    ).interactive()

    st.altair_chart(chart, use_container_width=True)

    st.subheader("📝 Recent Mood Entries")
    st.dataframe(df.tail(10).sort_values(by="timestamp", ascending=False))
else:
    st.warning("No mood logs found. Use the mood detector app first.")

