FROM python:3.12-slim

# Install system deps needed for psycopg2 (Postgres driver)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /code

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code (for now this is empty, we'll generate Django later)
COPY . .

EXPOSE 8000

