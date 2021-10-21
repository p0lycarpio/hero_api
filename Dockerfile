# Image de base
FROM python:3.9.6-alpine

# Dossier de travail dans l'image
WORKDIR usr/src/app

# Installation des dépendances
RUN apk update \
&& apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /usr/src/app/requirements.txt

# Ajout du ficher requirements
RUN pip install -r requirements.txt

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Entrypoint et migrations d'une bdd PgSQL
COPY herosite/entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh


ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
