FROM python:3.11-alpine

LABEL AUTHOR=mosesbwire91@gmail.com

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk update && apk add python3-dev mariadb-dev gcc musl-dev

RUN pip3 install -r requirements.txt

ARG ENV

ARG SECRET_KEY

ARG USERNAME

ARG HOST

ARG DATABASE

ARG PASSWORD

ENV ENV=$ENV

ENV SECRET_KEY=$SECRET_KEY

ENV USERNAME=$USERNAME

ENV HOST=$HOST

ENV DATABASE=$DATABASE

ENV PASSWORD=$PASSWORD

COPY . .

EXPOSE 5000

CMD ["gunicorn","--workers", "1", "--timeout", "1000",  "--bind", "0.0.0.0:5000", "api.v1.wsgi:app"]
