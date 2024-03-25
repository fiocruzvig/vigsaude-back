from pathlib import Path
import os
from .base import *

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']

DATABASES = {
    
}







