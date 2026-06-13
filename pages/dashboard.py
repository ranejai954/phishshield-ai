import streamlit as st

from database.db import (
    get_total_analyses,
    get_average_risk_score,
    get_threat_count
)

st.title("📊 PhishShield AI Dashboard")

total = get_total_analyses()

avg_score = get_average_risk_score()

critical = get_threat_count("CRITICAL")
high = get_threat_count("HIGH")
medium = get_threat_count("MEDIUM")
low = get_threat_count("LOW")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Analyses",
        total
    )

with col2:
    st.metric(
        "Average Risk Score",
        avg_score
    )

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.metric(
        "Critical Threats",
        critical
    )

with col4:
    st.metric(
        "High Threats",
        high
    )

col5, col6 = st.columns(2)

with col5:
    st.metric(
        "Medium Threats",
        medium
    )

with col6:
    st.metric(
        "Low Threats",
        low
    )