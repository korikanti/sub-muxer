
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', 5039008925:AAE19W2bcVJ45DoXLlkfuEyrm632QzzIRb8)
    APP_ID = os.environ.get('APP_ID',7287628)
    API_HASH = os.environ.get('API_HASH',6986f5d5aa82737cf7fb0c5b9492e732)

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1098504493').split(',')]

    DOWNLOAD_DIR = 'downloads'
