import streamlit as st

st.set_page_config(
    page_title="PhishShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ PhishShield AI")

st.subheader(
    "AI-Powered Phishing Detection & Threat Analysis Platform"
)

st.markdown("---")

st.markdown("""
### About PhishShield AI

PhishShield AI is an intelligent cybersecurity platform that helps users identify and analyze phishing emails, SMS messages, and suspicious communications using Artificial Intelligence.

The platform evaluates messages, calculates risk scores, identifies phishing indicators, and generates detailed security reports.
""")

st.markdown("---")

st.markdown("""
### Key Features

✅ AI-Powered Phishing Detection

✅ Risk Score Calculation

✅ Threat Level Classification

✅ Phishing Indicator Identification

✅ Detailed Security Recommendations

✅ PDF Report Generation

✅ MySQL-Based Analysis Storage

✅ Historical Analysis Tracking

✅ Security Analytics Dashboard
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        "🔍 Analyze suspicious emails, SMS messages, and links."
    )

with col2:
    st.info(
        "📊 View analytics and monitor phishing trends."
    )

with col3:
    st.info(
        "📄 Generate downloadable PDF security reports."
    )

st.markdown("---")

st.success(
    "Use the sidebar to navigate between Analyze, Dashboard, and History."
)

st.caption(
    "IBM SkillsBuild AI Internship Project | PhishShield AI v1.0"
)