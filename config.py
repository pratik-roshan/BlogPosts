import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:sql%40123@localhost:5432/blogdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False