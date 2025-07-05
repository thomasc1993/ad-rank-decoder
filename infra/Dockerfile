FROM python:3.11-slim

# Install dependencies
RUN pip install --no-cache-dir playwright openai google-cloud-bigquery google-cloud-storage slack_sdk && \
    playwright install chromium

# Copy source
COPY . /app
WORKDIR /app

# Entry point
CMD ["python", "main.py"]
