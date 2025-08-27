import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


conn = psycopg2.connect(
    host=os.getenv('HOST', 'postgres'),
    port=os.getenv('PORT', 5432),
    database=os.getenv('DATABASE', 'disaster_insurance'),
    user=os.getenv('USER', 'postgres'),
    password=os.getenv('PASSWORD', 'postgres')
)
cur = conn.cursor()

cur.execute("""  
    CREATE TABLE IF NOT EXISTS disaster (
        disasterNumber INT,
        incidentType TEXT,
        projectSize TEXT
    )
""")

conn.commit()

insert_query = """
    INSERT INTO disaster (disasterNumber,incidentType, projectSize)
    VALUES (%s, %s, %s)
"""
