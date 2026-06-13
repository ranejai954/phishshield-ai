import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="phishshield"
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