from pathlib import Path
import os
from .base import *



SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']

DATABASES = {
    
}







