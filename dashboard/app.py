import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Smart Waste Management Dashboard",
    page_icon="🗑️",
    layout="wide"
)

# ----------------------------------
# CONSTANTS
# ----------------------------------

CSV_FILE = "data/waste_log.csv"

# ----------------------------------
# FUNCTIONS
# ----------------------------------

def load_data():

    if not os.path.exists(CSV_FILE):

        return pd.DataFrame()

    try:

        return pd.read_csv(CSV_FILE)

    except:

        return pd.DataFrame()


def get_status_color(status):

    if status == "EMPTY":
        return "🟢"

    if status == "HALF FULL":
        return "🟡"

    return "🔴"


def build_gauge(value):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",

            value=value,

            title={
                "text":
                "Fill Level (%)"
            },

            gauge={
                "axis": {
                    "range":
                    [0, 100]
                },

                "steps": [

                    {
                        "range":
                        [0, 40]
                    },

                    {
                        "range":
                        [40, 80]
                    },

                    {
                        "range":
                        [80, 100]
                    }
                ]
            }
        )
    )

    fig.update_layout(
        height=300
    )

    return fig


# ----------------------------------
# TITLE
# ----------------------------------

st.title(
    "🗑️ Smart Waste Management System"
)

st.markdown(
    """
Real-Time IoT Based Bin Monitoring Dashboard
"""
)

# ----------------------------------
# LOAD DATA
# ----------------------------------

df = load_data()

if df.empty:

    st.warning(
        "No monitoring data available."
    )

    st.stop()

# ----------------------------------
# LATEST DATA
# ----------------------------------

latest = df.iloc[-1]

# ----------------------------------
# KPI SECTION
# ----------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Distance (cm)",
        latest["distance_cm"]
    )

with col2:

    st.metric(
        "Fill %",
        latest["fill_percentage"]
    )

with col3:

    st.metric(
        "Status",
        latest["status"]
    )

with col4:

    st.metric(
        "Alert",
        latest["alert"]
    )

# ----------------------------------
# GAUGE
# ----------------------------------

st.subheader(
    "Current Bin Level"
)

gauge = build_gauge(
    latest["fill_percentage"]
)

st.plotly_chart(
    gauge,
    use_container_width=True
)

# ----------------------------------
# FILL HISTORY
# ----------------------------------

st.subheader(
    "Historical Fill Trend"
)

line_chart = px.line(
    df,

    x="timestamp",

    y="fill_percentage",

    title=(
        "Waste Level Over Time"
    )
)

st.plotly_chart(
    line_chart,
    use_container_width=True
)

# ----------------------------------
# DISTANCE TREND
# ----------------------------------

st.subheader(
    "Distance Trend"
)

distance_chart = px.line(
    df,

    x="timestamp",

    y="distance_cm",

    title=(
        "Distance Readings"
    )
)

st.plotly_chart(
    distance_chart,
    use_container_width=True
)

# ----------------------------------
# STATUS COUNTS
# ----------------------------------

st.subheader(
    "Bin Status Distribution"
)

status_count = (
    df["status"]
    .value_counts()
    .reset_index()
)

status_count.columns = [
    "Status",
    "Count"
]

pie = px.pie(
    status_count,

    names="Status",

    values="Count",

    title=(
        "Status Distribution"
    )
)

st.plotly_chart(
    pie,
    use_container_width=True
)

# ----------------------------------
# ALERT ANALYTICS
# ----------------------------------

st.subheader(
    "Alert Analytics"
)

alerts = len(
    df[
        df["alert"]
        != "Normal"
    ]
)

st.info(
    f"Total Alerts Generated: {alerts}"
)

# ----------------------------------
# RECENT RECORDS
# ----------------------------------

st.subheader(
    "Recent Records"
)

st.dataframe(
    df.tail(20),
    use_container_width=True
)

# ----------------------------------
# DOWNLOAD CSV
# ----------------------------------

st.subheader(
    "Export Data"
)

csv = df.to_csv(
    index=False
)

st.download_button(

    label="Download CSV",

    data=csv,

    file_name=(
        "waste_log.csv"
    ),

    mime="text/csv"
)

# ----------------------------------
# SMART CITY VIEW
# ----------------------------------

st.header(
    "🏙 Smart City Multi-Bin View"
)

city_bins = pd.DataFrame({

    "Bin ID": [
        "BIN-101",
        "BIN-102",
        "BIN-103",
        "BIN-104",
        "BIN-105"
    ],

    "Fill %": [
        23,
        56,
        91,
        72,
        88
    ],

    "Status": [
        "EMPTY",
        "HALF FULL",
        "FULL",
        "HALF FULL",
        "FULL"
    ]
})

st.dataframe(
    city_bins,
    use_container_width=True
)

# ----------------------------------
# FULL BINS
# ----------------------------------

full_bins = city_bins[
    city_bins["Fill %"] >= 80
]

st.error(
    f"{len(full_bins)} bins "
    f"require immediate collection."
)

st.dataframe(
    full_bins,
    use_container_width=True
)

# ----------------------------------
# FOOTER
# ----------------------------------

st.markdown("---")

st.markdown(
    """
Built with ❤️ using
Python, Streamlit,
Plotly and IoT Concepts.
"""
)