from flask import Blueprint
#from app.app import create_celery_app

bptest1 = Blueprint('bptest1', __name__)

from . import views, tasks