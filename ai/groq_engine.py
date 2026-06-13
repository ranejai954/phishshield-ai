from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_phishing(text):
    prompt = f"""
You are a cybersecurity expert.

Analyze the following message for phishing or scam indicators.

Message:
{text}

Return:
1. Threat Level (Low, Medium, High, Critical)
2. Risk Score (0-100)
3. Key Indicators
4. Explanation
5. Recommendations

Keep the response concise and professional.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content