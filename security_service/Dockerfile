FROM ubuntu:22.04

RUN apt update && apt install -y gunicorn3 libpq-dev python3-pip

WORKDIR /security_service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /security_service

EXPOSE 5002

CMD ["gunicorn3", "--bind", "0.0.0.0:5002", "app:app"]