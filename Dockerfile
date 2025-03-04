# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python server script and requirements.txt
COPY https_server.py .

# Expose the Render-assigned port (default 8080)
EXPOSE 8080

# Command to run the server
CMD ["python3", "https_server.py"]
