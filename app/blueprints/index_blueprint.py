from flask import Blueprint
from flask import flash
from flask import render_template
from flask import url_for
from flask import redirect

from app import db
from app.models import User

bp = Blueprint(name='index', import_name=__name__)

@bp.route(rule='/', methods=['GET'])
def index():
    '''
    Home Page
    '''
    return render_template('index.html')