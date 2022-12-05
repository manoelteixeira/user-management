
from flask import Blueprint
from flask import flash
from flask import render_template
from flask import url_for
from flask import redirect
from flask_login import login_required
from flask_login import current_user

from app import db
from app.models import User
from app.forms import ChangePasswordForm

bp = Blueprint(name='profile', import_name=__name__)


@bp.route(rule='/profile', methods=['GET'])
@login_required
def profile():
    '''
    Display User Profile
    '''
    form = ChangePasswordForm()
    return render_template('profile.html',
                           form=form)