import streamlit as st
from datetime import datetime

from ai.groq_engine import analyze_phishing
from database.db import save_analysis
from reports.pdf_generator import generate_pdf

st.title("🛡️ Phishing Analyzer")

message = st.text_area(
    "Paste suspicious email, SMS, or message:"
)

if st.button("Analyze"):

    if message.strip():

        with st.spinner("Analyzing..."):
            result = analyze_phishing(message)

        # Generate unique analysis ID
        analysis_id = (
            "PH-" +
            datetime.now().strftime("%Y%m%d%H%M%S")
        )

        # Save analysis to MySQL
        save_analysis(
            analysis_id=analysis_id,
            input_type="Text",
            input_text=message,
            risk_score=result["risk_score"],
            threat_level=result["threat_level"],
            explanation=result["explanation"],
            recommendations=", ".join(
                result["recommendations"]
            )
        )

        # Generate PDF Report
        pdf_path = (
            f"exports/pdfs/{analysis_id}.pdf"
        )

        generate_pdf(
            filename=pdf_path,
            analysis_id=analysis_id,
            risk_score=result["risk_score"],
            threat_level=result["threat_level"],
            explanation=result["explanation"],
            recommendations=", ".join(
                result["recommendations"]
            )
        )

        st.success("Analysis Complete")

        st.subheader("Threat Analysis")

        st.metric(
            "Risk Score",
            f"{result['risk_score']}%"
        )

        if result["threat_level"] == "CRITICAL":

            st.error(
                f"Threat Level: {result['threat_level']}"
            )

        elif result["threat_level"] == "HIGH":

            st.warning(
                f"Threat Level: {result['threat_level']}"
            )

        elif result["threat_level"] == "MEDIUM":

            st.info(
                f"Threat Level: {result['threat_level']}"
            )

        else:

            st.success(
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

        st.caption(
            f"Analysis ID: {analysis_id}"
        )

        # Download PDF Button
        with open(pdf_path, "rb") as pdf_file:

            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_file,
                file_name=f"{analysis_id}.pdf",
                mime="application/pdf"
            )

    else:

        st.warning(
            "Please enter a message."
        )