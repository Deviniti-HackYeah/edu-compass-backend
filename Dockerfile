FROM python:3.11-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get -y install apt-utils
RUN apt-get -y install libpq-dev gcc iputils-ping wget g++
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY flask1.py flask1.py
COPY szkoly.json szkoly.json
ENV PYTHONUNBUFFERED=1
EXPOSE 3999
CMD ["sh","-c", "python -m flask --app flask1 run --host=0.0.0.0 --port=3999"]