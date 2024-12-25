# Use Python official image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Expose the application's port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
