FROM tiangolo/uvicorn-gunicorn:python3.11-slim

LABEL version="1.0.0"
LABEL description="Example Flask App"

# Create a non-root user
RUN useradd -m app
USER app

# Set the working directory
WORKDIR /app
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
EXPOSE 5000
ENV FLASK_APP=app.py

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]