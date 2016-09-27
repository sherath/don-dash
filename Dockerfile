FROM ubuntu:16.04
MAINTAINER Ash Wilson

#########
# Install Python, pip, Flask, and the CloudPassage SDK
#########
RUN apt-get update && \
    apt-get install -y \
    apt-transport-https \
    curl \
    python \
    python-pip

RUN pip install \
    flask \
    cloudpassage \
    pytest

#########
# Set up the CloudPassage repo, install the agent
#########
RUN echo 'deb https://production.packages.cloudpassage.com/debian debian main' | tee /etc/apt/sources.list.d/cloudpassage.list > /dev/null
RUN curl https://production.packages.cloudpassage.com/cloudpassage.packages.key | apt-key add -
RUN apt-get update && \
    apt-get install -y \
    cphalo

COPY ./ /app/
WORKDIR /app

ENV FLASK_APP=runner.py

EXPOSE 5000

CMD python -m flask run --host=0.0.0.0
