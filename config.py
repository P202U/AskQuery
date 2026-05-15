import os
import getpass


def get_google_api_key():
    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
    return os.environ["GOOGLE_API_KEY"]


TOP_K_RESULTS = 5
DB_URI = "postgresql+psycopg2://postgres:pass@localhost:5432/my_db"
MODEL_NAME = "gemini-1.5-flash"
THREAD_ID = "1"
