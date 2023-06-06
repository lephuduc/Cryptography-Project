FROM ubuntu:22.04

RUN apt-get update && apt install -y gunicorn3 python3-pip libpq-dev

RUN apt install -y wget

WORKDIR /opa-service

COPY . /opa-service

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN wget -q -O opa https://github.com/open-policy-agent/opa/releases/download/v0.53.0/opa_linux_amd64

RUN chmod +x opa

EXPOSE 8181

CMD "gunicorn3 --bind 0.0.0.0:8181 app:app"
