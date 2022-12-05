from flask import Blueprint
from flask import flash
from flask import render_template
from flask import url_for
from flask import redirect
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from sqlalchemy.exc import IntegrityError
from app import db
from app import login_manager
from app.models import User
from app.forms import LoginForm
from app.forms import RegisterForm
from app.forms import ChangePasswordForm

bp = Blueprint(name='auth', import_name=__name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    '''
    Redirect Unauthorized users to loging page
    '''
    flash("Please log in.")
    return redirect(url_for('auth.login'))

@bp.route('/register', methods=['GET','POST'])
def register():
    '''
    Register New User.
    '''
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(name=form.name.data,
                        username=form.username.data,
                        email=form.email.data,
                        password=form.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        except IntegrityError as e:
            args = e.args 
            if any('username' in arg for arg in args):
                flash('Username already in user')
            if any('email' in arg for arg in args):
                flash('Email already in use.')
            db.session.rollback()
    
    return render_template('register.html',
                           form=form)

@bp.route('/login', methods=['GET','POST'])
def login():
    '''
    Log in registered user.
    '''
    if current_user.is_authenticated:
        flash('Already logged in! Redirecting to your User Profile Page.')
        return redirect(url_for('profile.profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('Invalid Username.')
        elif not user.check_password(form.password.data):
            flash('Password is incorrect.')
        else:    
            login_user(user=user, remember=form.remember.data)
            return redirect(url_for('profile.profile'))
        
    return render_template('login.html',
                           form=form)
    
@bp.route('/logout', methods=['GET'])
@login_required
def logout():
    '''
    Log out user.
    '''
    logout_user()
    flash('User Logged off.')
    return redirect(url_for('auth.login'))


@bp.route('/change-password', methods=['POST'])
@login_required
def change_password():
    '''
    Change Password
    '''
    form = ChangePasswordForm()
    if form.validate_on_submit():
        user = User.query.get(current_user.id)
        equal_password = form.password.data == form.new_password.data
        valid_password = user.check_password(form.password.data)
        if not equal_password and valid_password:
            user.set_password(form.new_password.data)
            try:
                db.session.commit()
                flash('Your password has been changed.')
            except Exception as e:
                db.session.roolback()
                flash('Something whent wrong. Password could not be changed.')                
        elif equal_password:
            flash('Choose a different password.')
        elif not valid_password:
            flash('Password is incorrect.')
    return redirect(url_for('profile.profile'))

