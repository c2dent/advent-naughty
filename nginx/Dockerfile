FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

COPY abc0070033.fvds.ru.crt /etc/ssl
COPY abc0070033.fvds.ru.key /etc/ssl/private