from flask import Flask
import pandas as pd 
import os
from config import Config
from flask_sqlalchemy import SQLAlchemy
from app.models import Player

#Issue for this function is how to integrate into create_app

#create a temporary app and db that points to location of app db
temp = Flask(__name__)
temp.config.from_object(Config)
db = SQLAlchemy(temp)


#load data into db
df = pd.read_csv('app/static/data/players_20.csv')
df = df[:100]
for row in df.itertuples():
    id = getattr(row,'Index')
    sofifa_id=getattr(row,'sofifa_id')
    club=getattr(row,'club')
    country=getattr(row,'nationality')
    short_name=getattr(row,'short_name')
    long_name=getattr(row,'long_name')
    
    player = Player(player_id=id,sofifa_id=sofifa_id,club=club,country=country,
    short_name=short_name,long_name=long_name)
    try:
        db.session.add(player)
        db.session.commit()
    except:
        print("player profile already loaded")
        db.session.rollback()
        pass


