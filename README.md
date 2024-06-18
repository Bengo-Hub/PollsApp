# SETTING UP THE ENVIRONMNET

## step 1: instal python
install python 3.9+ 3.12.3
unbuntu - use terminal 
windows - download and install python from the internet, add python to path when installing, also go with custom to be able to select custom features

## step 2: create env
### ubuntu - python3 -m venv name_of_env e.g env
### windows - python -m venv name_of_env e.g env

## step 3: activate or deactivate env
### ubuntu 
1. . env/bin/activate or deactovate e.g . env/bin/deactivate
2. source env/bin/activate or deactivate

### windows - .\env\Scripts\activate or deactivate

## step 4: Installl django within the virtual env(env has to be activated before running this command)- make sure you have internet connection
- pip install django - this command picks the latest version of django but if you need to specify a custom version of django then run the command bellow
- pip install django==4.2.1 - check a specific release here https://docs.djangoproject.com/en/5.0/releases/

## step 5: Creating a django project and confirming that it works! 
```sh 
django-admin startproject PollsApp
```

- once you install your project requirements, save them in a requirements.txt file using the command pip freeze > requirements.txt
- install requirements from txt file - pip install -r requirements.txt