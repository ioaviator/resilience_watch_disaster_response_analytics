from dotenv import load_dotenv
from include.db_connect import conn, cur, insert_query
from include.extract import extract_data

load_dotenv()


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
