#!/bin/bash

# Установите значения переменных среды
export CERTS_PATH="/etc/letsencrypt/live"
export OPTIONS_SSL_PATH="/etc/letsencrypt/options-ssl-nginx.conf"
export DH_PARAMS_PATH="/etc/letsencrypt/ssl-dhparams.pem"
export DOMEN="abc0070033.fvds.ru"  # Укажите домен, который вы используете


sed -i "s|{{CERTS_PATH}}|${CERTS_PATH}|g" docker-compose.prod.yml
sed -i "s|{{OPTIONS_SSL_PATH}}|${OPTIONS_SSL_PATH}|g" docker-compose.prod.yml
sed -i "s|{{DH_PARAMS_PATH}}|${DH_PARAMS_PATH}|g" docker-compose.prod.yml
sed -i "s|{{DOMEN}}|${DOMEN}|g" docker-compose.prod.yml

# Запустите docker-compose
docker-compose -f docker-compose.prod.yml up -d --build
