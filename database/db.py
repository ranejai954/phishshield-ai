import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


def save_analysis(
    analysis_id,
    input_type,
    input_text,
    risk_score,
    threat_level,
    explanation,
    recommendations
):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO analyses
    (
        analysis_id,
        input_type,
        input_text,
        risk_score,
        threat_level,
        explanation,
        recommendations
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        analysis_id,
        input_type,
        input_text,
        risk_score,
        threat_level,
        explanation,
        recommendations
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()


def get_all_analyses():
    conn = get_connection()

    cursor = conn.cursor(
        dictionary=True
    )

    cursor.execute("""
        SELECT *
        FROM analyses
        ORDER BY created_at DESC
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data