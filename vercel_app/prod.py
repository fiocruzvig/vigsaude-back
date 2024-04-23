from pathlib import Path
from dotenv import load_dotenv
import os
from .base import *
load_dotenv() 


SECRET_KEY = os.getenv("API_KEY")
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']

DATABASES = {

    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('NAME_PG'),
        'USER':os.getenv('USER_PG'),
        'PASSWORD':os.getenv('PASSWORD_PG'),
        'HOST':os.getenv('HOST_PG'),
        'PORT':os.getenv('PORT_PG')
    }

}









