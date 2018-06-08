FROM python:3.6-alpine

RUN mkdir /storage

WORKDIR ./code

ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ADD . ./

ENV WEB_SERVER_PORT 8000

ENV ALLOWED_HOSTS '["web"]'

EXPOSE ${WEB_SERVER_PORT}

ENTRYPOINT ["./entrypoint.sh"]
