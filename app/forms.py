from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,RadioField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class KickoffForm(FlaskForm):
    choose_player1 = BooleanField(str('Player 1'))
    choose_player2 = BooleanField(str('Player 2'))
    submit = SubmitField('Choose!')

    def validate_selection(self, choose_player1, choose_player2):
        if choose_player1.data and choose_player2.data:
            print("error")
            raise ValidationError("Please choose only one player")
        elif not choose_player1.data and not choose_player2.data:
            print("error")
            raise ValidationError("Please choose a player")


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    team = StringField('Favorite Football Team')
    player = StringField('Favorite Football Player')
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email address already taken.")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username already taken.")