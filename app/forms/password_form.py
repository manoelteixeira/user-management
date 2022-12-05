from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import EmailField
from wtforms import SubmitField

from wtforms.validators import DataRequired
from wtforms.validators import EqualTo
from wtforms.validators import Length


class ChangePasswordForm(FlaskForm):
    password = PasswordField(label='Current password',
                             validators=[DataRequired()])
    new_password = PasswordField(label='New Password',
                             validators=[DataRequired(),
                                         Length(min=6,
                                                message='Password must have at least 6 characters')
                                         ],
                             description='At Least 6 characters.')
    confirm = PasswordField(label='Re-enter password',
                            validators=[DataRequired(),
                                        EqualTo(fieldname='new_password',
                                                message='Password must match'),
                                        ])
    submit = SubmitField(label='Continue')
    
class ForgotPasswordForm(FlaskForm):
        username = StringField(label='Username',
                               validators=[DataRequired()])
        email = EmailField(label='Email',
                           validators=[DataRequired()])