from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    team = StringField('Favorite Football Team', validators=[DataRequired, Email()])
    player = StringField('Favorite Football Player', validators=[DataRequired, Email()])
    email = StringField('Email', validators=[DataRequired, Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired, EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = user.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email address already taken.")

    def validate_username(self, username):
        user = user.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username already taken.")