# frontend_app.py

from Deepspeak import main_streamlit_app
from dotenv import load_dotenv
load_dotenv()
API_BASE = os.getenv("API_BASE_URL")

if __name__ == "__main__":
    main_streamlit_app()