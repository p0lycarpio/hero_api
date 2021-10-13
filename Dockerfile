# Image de base, de quoi avons-nous besoin ? Rappelez-vous que l'on veut faire léger !
FROM python:3.9.6-alpine

# Dossier de travail dans l'image
WORKDIR usr/src/app

# Installation des dépendances
RUN apk update \
&& apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /usr/src/app/requirements.txt

# Ajout du ficher requirements
RUN pip install -r requirements.txt

# Ajout du reste du code de l'application
#COPY herosite .

#CMD ["python", "manage.py", "runserver"]