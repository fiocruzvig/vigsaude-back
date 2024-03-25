
from pathlib import Path
from dotenv import load_dotenv
import os
from .base import *
load_dotenv() 

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("API_KEY")
DEBUG = True

DATABASES = {
    
}






