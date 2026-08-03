import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from uberdrive_analytics.data_loader import UberDataLoader
from uberdrive_analytics.eda_engine import UberEDAEngine

st.set_page_config(
    page_title="UberDrive Analytics Engine",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 UberDrive Analytics Engine & Intelligence Dashboard")
st.markdown("Developed by **Nachiket Gadilohar** | [GitHub](https://github.com/nachiket0987) | [LinkedIn](https://linkedin.com/in/nachiket-gadilohar-profile/)")

data_path = Path(__file__).parent / "Uber Drives.csv"

@st.cache_data
def get_data():
    loader = UberDataLoader(str(data_path))
    return loader.load_clean_data()

try:
    df = get_data()
    engine = UberEDAEngine(df)
    metrics = engine.summary_metrics()

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Trips", f"{metrics['total_trips']:,}")
    col2.metric("Total Distance", f"{metrics['total_miles']:,} mi")
    col3.metric("Avg Trip Distance", f"{metrics['avg_trip_miles']} mi")
    col4.metric("Avg Duration", f"{metrics['avg_duration_min']} min")
    col5.metric("Business Trips", f"{metrics['business_trips_pct']}%")

    st.markdown("---")

    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("⏰ Hourly Ride Distribution")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x=engine.hourly_distribution().index, y=engine.hourly_distribution().values, palette="Blues_d", ax=ax)
        ax.set_xlabel("Hour of Day")
        ax.set_ylabel("Number of Trips")
        st.pyplot(fig)

    with col_right:
        st.subheader("🎯 Trip Purpose Breakdown")
        fig, ax = plt.subplots(figsize=(8, 4))
        purpose_counts = engine.trips_by_purpose().head(8)
        sns.barplot(x=purpose_counts.values, y=purpose_counts.index, palette="viridis", ax=ax)
        ax.set_xlabel("Trip Count")
        st.pyplot(fig)

    col_bottom_l, col_bottom_r = st.columns(2)

    with col_bottom_l:
        st.subheader("📍 Top Pickup Hotspots")
        st.dataframe(engine.top_pickup_locations(10).reset_index().rename(columns={"index": "Location", "START*": "Count"}))

    with col_bottom_r:
        st.subheader("🏁 Top Drop-off Hotspots")
        st.dataframe(engine.top_dropoff_locations(10).reset_index().rename(columns={"index": "Location", "STOP*": "Count"}))

except Exception as e:
    st.error(f"Error loading dashboard data: {e}")
