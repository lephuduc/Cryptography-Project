FROM python:3.10.11

WORKDIR /product-service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /product-service

EXPOSE 5003

CMD  ["gunicorn3", "--bind", "0.0.0.0:5003", "app:app"]