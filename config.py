import os
import getpass
from dotenv import load_dotenv

load_dotenv()


def get_google_api_key():
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        api_key = getpass.getpass("Enter your Google AI API key: ")
        os.environ["GOOGLE_API_KEY"] = api_key

    return api_key


TOP_K_RESULTS = 5
DB_URI = "postgresql://makima:Traumerei%4020139%23@localhost:5432/queryme"
MODEL_NAME = "gemini-2.5-flash"
THREAD_ID = "1"
