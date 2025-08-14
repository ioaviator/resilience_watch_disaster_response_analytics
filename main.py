import requests
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

URL = os.getenv('API_URL')


conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='disaster_insurance',
    user='postgres',
    password='1234'
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

def extract_data():
    response = requests.get(URL)

    return response.json()['PublicAssistanceFundedProjectsDetails']


insurance_data = []
def main():
    data = extract_data()

    # print(data)
    insurance_data.extend(data)


    postgres_data = [ (data['disasterNumber'], data['incidentType'], data['projectSize']) for data in insurance_data ]

    # print(len(postgres_data))

    cur.executemany(insert_query, postgres_data)

    conn.commit()

    cur.close()
    conn.close()

    print('data loaded successfully')

    return None

if __name__ == '__main__':
    main()