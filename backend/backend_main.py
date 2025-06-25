# backend_main.py

from Deepspeak import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend_main:app", host="0.0.0.0", port=8000)