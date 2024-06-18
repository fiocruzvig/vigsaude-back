from pathlib import Path
from dotenv import load_dotenv
import os
from .base import *
load_dotenv() 
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
MONGO_DATABASE = {
      'DRIVER': os.environ.get("MONGO_DRIVER"),
      'USER': os.environ.get('MONGO_USER'),
      'PASSWORD':os.environ.get('MONGO_PASSWORD'),
      'HOST':os.environ.get('MONGO_HOST'),
      'PORT':''
}
DATABASES = {

    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('NAME'),
        'USER':os.environ.get('USER'),
        'PASSWORD':os.environ.get('PASSWORD'),
        'HOST':os.environ.get('HOST'),
        'PORT':os.environ.get('PORT')
    }

}









