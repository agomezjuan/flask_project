import os
from dotenv import load_dotenv

load_dotenv()

# Grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

# Set the secret key
SECRET_KEY = os.environ.get('SECRET_KEY')

# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
