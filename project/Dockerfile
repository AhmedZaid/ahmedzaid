# As Scrapy runs on Python, I choose the official Python 3 Docker image.
FROM python:3.9.6

# Set the working directory to /usr/src/app.
WORKDIR /scraper/src/docker

# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./

RUN pip install PEP517

RUN pip install --upgrade pip setuptools wheel
# Install Scrapy specified in requirements.txt.
RUN pip install --no-cache -r  requirements.txt

# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . .

# Run the crawler when the container launches.
CMD [ "python3", "project/main.py" ]