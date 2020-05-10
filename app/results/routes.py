from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, current_app
from flask_login import current_user, login_required
from app import db
from app.models import User, Result, Player
from app.results import bp

@bp.route('/players')
def player_results():
    top_players = Player.query.order_by(Player.elo_ranking.desc()).limit(10).all()
    return render_template('results/results.html',top_players=top_players)