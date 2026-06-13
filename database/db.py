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


# =========================
# Dashboard Functions
# =========================

def get_total_analyses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM analyses"
    )

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total


def get_average_risk_score():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT AVG(risk_score) FROM analyses"
    )

    avg_score = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return round(avg_score or 0, 2)


def get_threat_count(threat_level):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM analyses
        WHERE threat_level = %s
        """,
        (threat_level,)
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count