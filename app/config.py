from dotenv import load_dotenv
import os
load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS')


class AdminConfig:
    USER_ADMIN_USERNAME = os.getenv('USER_ADMIN_USERNAME')
    USER_ADMIN_PASSWORD = os.getenv('USER_ADMIN_PASSWORD')
    USER_ADMIN_EMAIL = os.getenv('USER_ADMIN_EMAIL')
