FROM python:3.10

WORKDIR /app

# Copy the requirements and install them
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all project files (including your .py scripts)
COPY . .

# Change demo.py to your actual main entry file
CMD ["python", "image_captioning_app.py"]