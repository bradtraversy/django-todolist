FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code; exit 0
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/