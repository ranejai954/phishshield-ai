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

        st.subheader("Threat Analysis")

        st.metric(
            "Risk Score",
            f"{result['risk_score']}%"
        )

        st.write(
            f"Threat Level: {result['threat_level']}"
        )

        st.write("### Indicators")
        for indicator in result["indicators"]:
            st.write(f"• {indicator}")

        st.write("### Explanation")
        st.write(result["explanation"])

        st.write("### Recommendations")
        for recommendation in result["recommendations"]:
            st.write(f"• {recommendation}")

    else:
        st.warning("Please enter a message.")