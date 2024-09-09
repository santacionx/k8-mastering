# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the app directory contents into the container
COPY ./app /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
