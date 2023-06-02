FROM python:3.8

RUN apt-get update && apt install -y gunicorn3

WORKDIR /opa-service

COPY . /opa-service

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install -r /opa-service/requirements.txt

CMD ["./entrypoint.sh"]
