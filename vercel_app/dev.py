
from pathlib import Path
from dotenv import load_dotenv
import os
from .base import *
load_dotenv() 

SECRET_KEY = os.getenv("API_KEY")
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']

DATABASES = {

    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('NAME'),
        'USER':os.getenv('USER'),
        'PASSWORD':os.getenv('PASSWORD'),
        'HOST':os.getenv('HOST'),
        'PORT':os.getenv('PORT')
    }

}






