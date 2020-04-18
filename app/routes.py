from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegistrationForm, KickoffForm
from flask_login import current_user, login_user, logout_user
from app.models import User, Player, Result
from app import db
from config import Config
import random

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/kickoff', methods=['GET','POST'])
def kickoff():
    #generate players to compare using random numbers
    def get_players(player1=None,player2=None):
        player1 = random.randint(0,app.config['NUM_PLAYERS']-1) if player1 is None else player1
        player2 = random.randint(0,app.config['NUM_PLAYERS']-1) if player2 is None else player2
        while(player2 == player1):
            player2 = random.randint(0,app.config['NUM_PLAYERS']-1)
        return player1,player2

    player1,player2 = get_players()
    player1 = Player.query.get(int(player1))
    player2 = Player.query.get(int(player2))

    img1 = url_for('static',filename='img/'+str(player1.sofifa_id)+'.png')
    img2 = url_for('static',filename='img/'+str(player2.sofifa_id)+'.png')
    form = KickoffForm()

    if form.validate_on_submit():
        selection = 0
        if form.choose_player1.data:
            selection = player1.player_id
        else:
            selection = player2.player_id
        
        result = Result(player1_id=player1.player_id, player2_id=player2.player_id, 
                selection=selection)
        db.session.add(result)
        db.session.commit()
        return redirect(url_for('kickoff'))
    return render_template('kickoff.html', form=form, player1=player1, player2=player2, 
            img1 = img1, img2=img2)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return('Invalid username or password')
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
                player=form.player.data, team=form.team.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user.")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

