FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && pip3 install yfinance --upgrade --no-cache-dir \
  && pip3 install pandas

# ENTRYPOINT /var/app/src && python3 historical.py
