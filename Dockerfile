FROM python:3.10.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt install -y libpq-dev gcc python3-dev musl-dev gettext

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./config/entrypoint.sh .

COPY . .
