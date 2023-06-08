FROM ubuntu:22.04

RUN apt-get update && apt install -y gunicorn3 python3-pip libpq-dev

WORKDIR /product-service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /product_service

EXPOSE 5003

CMD ["gunicorn3", "--bind", "0.0.0.0:5003", "app:app"]
