from app import create_app, db
from app.models.card import Card

my_app = create_app()
with my_app.app_context():
    db.session.add(Card(message="dont stay up late, it will make you old", likes_count=0))
    db.session.add(Card(message="a social media platform called fakebook", likes_count=0))
    db.session.add(Card(message="I think then I code", likes_count=0))
    db.session.add(Card(message="never leave your keys in the car", likes_count=0))
    db.session.add(Card(message="knock knock... nothing I dont know any jokes", likes_count=0))
    db.session.commit()