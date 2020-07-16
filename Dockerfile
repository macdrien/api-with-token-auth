FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get install -y python3-pip python3.8-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python3.8 -m pip install -r requirements.txt

COPY . /app
