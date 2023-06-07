FROM python:3.10.11

WORKDIR /product-service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /product_service

EXPOSE 5003

CMD ["python3", "app.py"]