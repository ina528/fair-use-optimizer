import streamlit as st
import pandas as pd
from logic import calculate_scores

# ------------------------------
# Title
st.set_page_config(page_title="Fair-Use Resource Optimizer", layout="wide")
st.title("🏆 Fair-Use Resource Optimizer")

# ------------------------------
# Load Data
df = pd.read_csv("data/requests.csv")

# ------------------------------
# Sidebar: Adjust weights
st.sidebar.header("Adjust Score Weights")
attendance_weight = st.sidebar.slider("Attendance Weight", 0.0, 2.0, 0.6)
priority_weight = st.sidebar.slider("Priority Weight", 0.0, 2.0, 0.3)
usage_weight = st.sidebar.slider("Past Usage Weight", 0.0, 2.0, 0.4)

# ------------------------------
# Calculate Scores
df["score"] = (
    attendance_weight * df["attendance"] +
    priority_weight * df["priority"] -
    usage_weight * df["past_usage"]
)
scored_df = df.sort_values("score", ascending=False).reset_index(drop=True)

# ------------------------------
# Show Scores Table
st.subheader("📊 Team Scores")
st.dataframe(scored_df.style.background_gradient(subset=["score"], cmap="Greens"))

# ------------------------------
# Highlight Winner
winner = scored_df.iloc[0]
st.success(f"🏅 Resource allocated to {winner['group']} with score {winner['score']:.2f}")

# ------------------------------
# Optional: Show top 2 teams
st.subheader("Top 2 Teams")
st.table(scored_df.head(2))

