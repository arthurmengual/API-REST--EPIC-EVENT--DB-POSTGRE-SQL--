## Table of Contents

1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)

### General Info

---

Epicevent est une entreprise de conseil et de gestion dans l'événementiel qui répond aux besoins des start-up voulant organiser des « fêtes épiques ». Ce repository contient le logiciel de gestion de la relation client (CRM) de l'entreprise, qui effectue le suivi de tous les clients et événements.

### Logo

![softdesk](https://user.oc-static.com/upload/2020/09/22/16007804386673_P10.png)

## Technologies

---

A list of technologies used within the project:

- [Python3](https://example.com): Version 3.9.7
- CF requirements.txt

## Installation

---

A little intro about the installation.

`

## API AND DATABASE

$ python3 venv env
$ source env/bin/activate
$ git clone https://github.com/arthurmengual/P12.git
$ pip install -r requirements.txt
$ cd p12
$ sudo apt update
$ sudo apt install postgresql postgresql-contrib
$ sudo -i -u postgres
$ psql
$ sudo -u postgres createuser --interactive
$ sudo -u postgres createdb 'db name'
==> go to app settings and configure the database like this:

DATABASES = {
"default": {
"ENGINE": "django.db.backends.postgresql_psycopg2",
"NAME": "db name",
"USER": "username",
"PASSWORD": "pswd",
"HOST": "localhost",
"PORT": "",
}
}

$ ./manage.py migrate
$ ./manage.py runserver

```
## API Documentation

https://documenter.getpostman.com/view/17474735/UVypzHf3

```
