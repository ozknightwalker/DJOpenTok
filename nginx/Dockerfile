FROM nginx:latest

WORKDIR /nginx

ADD ./entrypoint ./

ENV WEB_SERVER_PORT 8000

ADD ./djopentok.template /etc/nginx/conf.d/django.template

ENTRYPOINT ["./entrypoint"]
