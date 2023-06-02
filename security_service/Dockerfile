FROM python:3.10.11

WORKDIR /user_service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /signin

EXPOSE 5002

CMD ["python3", "app.py"]