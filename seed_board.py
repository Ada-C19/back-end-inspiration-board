from app import create_app, db
from app.models.board import Board

my_app = create_app()
with my_app.app_context():
    db.session.add(Board(title="reminders", owner="Amber"))
    db.session.add(Board(title="capstone ideas", owner="Amber"))
    db.session.add(Board(title="quotes",owner="Areeg"))
    db.session.add(Board(title="advice",owner="Gabby"))
    db.session.add(Board(title="jokes",owner="Angelica"))
    db.session.commit()