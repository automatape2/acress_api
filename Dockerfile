# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

RUN apt update
RUN apt-get --fix-broken install -y libnss3 libgconf-2-4 libxi6 libgdk-pixbuf2.0-0 libxrandr2 libatk1.0-0 libx11-xcb1 libgbm1


# Install Chrome (google-chrome --version)
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# COPY google-chrome-stable_current_amd64.deb /code/
RUN dpkg -i google-chrome-stable_current_amd64.deb || true
RUN apt-get install -f -y

# Install ChromeDriver (https://googlechromelabs.github.io/chrome-for-testing/#stable)
RUN wget https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.78/linux64/chromedriver-linux64.zip
# COPY chromedriver-linux64.zip /code/
RUN unzip chromedriver-linux64.zip
RUN mv ./chromedriver-linux64/chromedriver /usr/bin/chromedriver
# RUN rm -R -f ./chromedriver-linux64
RUN chown root:root /usr/bin/chromedriver
RUN chmod +x /usr/bin/chromedriver

COPY requirements.txt /code/
# RUN pip3.12 install --disable-pip-version-check --target . --upgrade -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/
