FROM ubuntu:22.04

WORKDIR /served_html_service

COPY requirements.txt .

RUN apt update

RUN apt install -y gunicorn3 python3-pip libpq-dev

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN apt install -y curl

COPY . /served_html_service

EXPOSE 8000

CMD  ["gunicorn3", "--bind", "0.0.0.0:8000", "app:app"]
