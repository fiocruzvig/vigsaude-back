
from pathlib import Path
from dotenv import load_dotenv
import os
from .base import *
load_dotenv() 

SECRET_KEY = os.getenv("API_KEY")
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']

DATABASES = {
    
}






