# Dockerfile

FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libgtk2.0-dev \
    libglib2.0-0 \
    libsm6 \
    libxrender-dev \
    libxext6 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "backend_main.py"]
