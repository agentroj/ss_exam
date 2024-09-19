# Use the official Python image as a base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the app's code into the container
COPY . /app/

# Expose the port on which the app runs
EXPOSE 8765

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8765"]
