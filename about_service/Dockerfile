FROM ubuntu:22.04

RUN apt update && apt install -y gunicorn3 libpq-dev python3-pip

WORKDIR /about_service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /about_service

EXPOSE 5001

CMD ["gunicorn3", "--bind", "0.0.0.0:5001", "app:app"]