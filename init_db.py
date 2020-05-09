from flask import Flask
import os
from config import Config
from flask_sqlalchemy import SQLAlchemy
from app.models import Player
import csv

#Issue for this function is how to integrate into create_app

#create a temporary app and db that points to location of app db
temp = Flask(__name__)
temp.config.from_object(Config)
db = SQLAlchemy(temp)


#load data into db
with open('app/static/data/players_20.csv',encoding="utf8") as csvfile:
    df = csv.DictReader(csvfile, delimiter=',')
    index = 0
    for row in df:
        player_id = index
        sofifa_id=row["sofifa_id"]
        club=row['club']
        country=row['nationality']
        short_name=row['short_name']
        long_name=row['long_name']
        index +=1
        
        player = Player(player_id=player_id,sofifa_id=sofifa_id,club=club,country=country,
        short_name=short_name,long_name=long_name,elo_ranking=1600,cumulative_score=1600,
        num_selections=1)

        try:
            db.session.add(player)
            db.session.commit()
        except:
            print("Player already loaded")
            pass
        
        if index>100:
            break

