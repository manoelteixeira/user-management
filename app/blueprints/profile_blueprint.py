
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

# @bp.route(rule='/profile', methods=['GET', 'POST'])
# @login_required
# def profile():
#     form = ChangePasswordForm()
#     if form.validate_on_submit():
#         user = User.query.get(current_user.id)
#         equal_password = form.password.data == form.new_password.data
#         valid_password = user.check_password(form.password.data)
#         if not equal_password and valid_password:
#             user.set_password(form.new_password.data)
#             try:
#                 db.session.commit()
#                 flash('Your password has been changed.')
#             except Exception as e:
#                 db.session.roolback()
#                 flash('Something whent wrong. Password could not be changed.')                
#         elif equal_password:
#             flash('Choose a different password.')
#         elif not valid_password:
#             flash('Password is incorrect.')
        
#     return render_template('profile.html',
#                            form=form)

@bp.route(rule='/profile', methods=['GET'])
@login_required
def profile():
    form = ChangePasswordForm()
    return render_template('profile.html',
                           form=form)