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
df = csv.DictReader('app/static/data/players_20.csv', delimiter=',')

index = 0
for row in df:
    id = index
    sofifa_id=['sofifa_id']
    club=['club']
    country=['nationality']
    short_name=['short_name']
    long_name=['long_name']
    index +=1
    
    player = Player(player_id=id,sofifa_id=sofifa_id,club=club,country=country,
    short_name=short_name,long_name=long_name)
    try:
        db.session.add(player)
        db.session.commit()
    except:
        print("player profile already loaded")
        db.session.rollback()
        pass


