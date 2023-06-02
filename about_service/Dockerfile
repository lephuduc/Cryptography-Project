FROM python:3.10.11

WORKDIR /about_service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /about_service

EXPOSE 5001

CMD ["python3", "app.py"]