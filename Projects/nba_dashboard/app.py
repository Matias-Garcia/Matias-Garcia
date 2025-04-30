import streamlit as st
from scraper import fetch_nba_scores_json
import pandas as pd
import time

st.set_page_config(
    page_title="🏀 Live NBA Scoreboard",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.title("🏀 Live NBA Scoreboard")

placeholder = st.empty()
REFRESH_SECONDS = 60

while True:
    df = fetch_nba_scores_json()

    with placeholder.container():
        if df.empty:
            st.warning("No games found—check your network or scraper.")
        else:
            st.dataframe(df, use_container_width=True)

            st.subheader("Away Scores")
            st.bar_chart(df.set_index("away_team")["away_score"])
            st.subheader("Home Scores")
            st.bar_chart(df.set_index("home_team")["home_score"])

        st.caption(f"Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    time.sleep(REFRESH_SECONDS)
