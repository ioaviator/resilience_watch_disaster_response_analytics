import requests
import os
from dotenv import load_dotenv

load_dotenv()


URL = os.getenv('API_URL')

def extract_data():
    response = requests.get(URL)

    return response.json()['PublicAssistanceFundedProjectsDetails']