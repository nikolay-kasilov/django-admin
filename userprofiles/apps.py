from django.apps import AppConfig
from fastapi import FastAPI
app = FastAPI()

class UserprofilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userprofiles'
    verbose_name = 'Профили пользователей'
