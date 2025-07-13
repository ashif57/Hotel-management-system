# config.py
import os
from dotenv import load_dotenv

load_dotenv()



class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        os.getenv('DA_USER'),
        os.getenv('DA_PASSWORD'),
        os.getenv('DA_HOST'),
        os.getenv('DA_PORT'),
        os.getenv('DA_DATABASE')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'samplex'  # Needed for sessions/login
