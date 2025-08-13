import os
import psycopg2

import requests
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('URL')


DB_CONFIG = {
    "host": "localhost",   
    "port": 5434,
    "database": "disaster_response",
    "user": "admin",
    "password": "admin"
}

conn = psycopg2.connect(**DB_CONFIG)
# conn = psycopg2.connect(
#     host="localhost",
#     port=5434,
#     database="disaster_response",
#     user="admin",
#     password="admin")

cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS disaster (
    disasterNumber INT PRIMARY KEY,
    incidentType TEXT,
    projectSize TEXT
)
""")

insert_query = """
  INSERT INTO disaster (disasterNumber, incidentType, projectSize)
  VALUES (%s, %s, %s)
  ON CONFLICT (disasterNumber) DO NOTHING
"""






def extract_data():
  response = requests.get(URL)
  data = response.json()['PublicAssistanceFundedProjectsDetails']
  return data


disaster_data = []

def main():
  data = extract_data()

  disaster_data.extend(data)
  selected_data = [(data['disasterNumber'], data['incidentType'], data['projectSize'])   for data in disaster_data]

  cur.executemany(insert_query, selected_data)

  conn.commit()
  cur.close()
  conn.close()

  print(disaster_data[1])

  return



if __name__ == '__main__':
  main()