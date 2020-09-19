# reserveTime

## --Description

Welcome to reserveTime.

It is a website to find a table from any restaurants for any occasion. You can make your reservation easily, we also have payment system for making reservetion more clear.

How process going on website?

When you include reserveTime you will see restaurants and cafes, then you can filter restaurants by cuisines and city. If you find appropriate restaurant for you, then pass personal page of this restaurant and in this page you can get all needed informations about restaurant. If everything okay, you can find table and complete reservation.

# Installation

## First you need to download files to your computer

```
git clone https://github.com/ruhinshukurlu/reserveTime.git
```

## Install and activate Vitual Environment

```
sudo apt install python3-pip
```
```
sudo apt install python3-venv
```
```
python3.7 -m venv my_env
```
```
source my_env/bin/activate
```

## Install dependencies 

```
pip install -r requirements.txt

```

## Run docker

After successfuly installed dependecies you need to Build docker bellow command:

```
cd reserveTime/_development/
```
```
docker-compose up -d
```
```
cd ../
```

## Superuser

Create superusers using the createsuperuser command and you need to include email and password for superuser:

```
python manage.py createsuperuser
```

## Run server

```
./manage.py runserver
```

Now you can run server and include reserveTime using this url address http://127.0.0.1:8000/
