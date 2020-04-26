from app import app, db
import os
from app.models import Player, User
from sqlalchemy.exc import InvalidRequestError
import unittest

class TestCase(unittest.TestCase):
    def setUp(self):
        basedir = os.getcwd()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    def test_player_db(self):
        player = Player(player_id=10000, short_name='Test')
        
        try:
            db.session.add(player)
            db.session.commit()
        except InvalidRequestError:
            print("db session rollback")
            db.session.rollback()
            db.session.add(player)
            db.session.commit()

        player_returned = Player.query.get(10000)
        assert player_returned.player_id == 10000
    
if __name__ == "__main__":
    unittest.main()


    


