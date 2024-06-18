
from pathlib import Path
from dotenv import load_dotenv
import os
from .base import *
load_dotenv() 

SECRET_KEY = os.getenv("API_KEY")
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
MONGO_DATABASE = {
      'DRIVER': os.getenv('DRIVER_DOCKER_MONGO'),
      'USER': os.getenv('USER_DOCKER_MONGO'),
      'PASSWORD':os.getenv('PASSWORD_DOCKER_MONGO'),
      'HOST':os.getenv('HOST_DOCKER_MONGO'),
      'PORT':os.getenv('PORT_DOCKER_MONGO')
}
DATABASES = {
      'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('NAME_DOCKER_PG'),
        'USER':os.getenv('USER_DOCKER_PG'),
        'PASSWORD':os.getenv('PASSWORD_DOCKER_PG'),
        'HOST':os.getenv('HOST_DOCKER_PG'),
        'PORT':os.getenv('PORT_DOCKER_PG')
    }

}