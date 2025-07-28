# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /usr/src/app

# Copy dependency files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full scrapy project into the image
COPY . .

# Default command to run the spider
CMD ["scrapy", "crawl", "aajtak"]
