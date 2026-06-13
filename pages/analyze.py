import streamlit as st
from ai.groq_engine import analyze_phishing

st.title("🛡️ Phishing Analyzer")

message = st.text_area(
    "Paste suspicious email, SMS, or message:"
)

if st.button("Analyze"):
    if message.strip():

        with st.spinner("Analyzing..."):

            result = analyze_phishing(message)

        st.success("Analysis Complete")

        st.markdown(result)

    else:
        st.warning("Please enter a message.")