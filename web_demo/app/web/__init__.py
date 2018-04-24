from flask import Blueprint

web = Blueprint('web',__package__)

from app.web import problem
from app.web import user