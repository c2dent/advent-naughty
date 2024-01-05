FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY /etc/letsencrypt/live/abc0070033.fvds.ru/fullchain.pem /etc/cert/
COPY /etc/letsencrypt/live/abc0070033.fvds.ru/privkey.pem /etc/cert/