FROM python:3.8

WORKDIR /workspace

ADD ./src/requirements.txt /workspace/

RUN pip install -r requirements.txt