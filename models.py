from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Survey(db.Model):

    __tablename__ = "Survey"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    q1 = db.Column(db.Text, nullable=False)
    q2 = db.Column(db.Text, nullable=False)
    q3 = db.Column(db.Integer, nullable=False)
    q4 = db.Column(db.Text, nullable=False)
    q5 = db.Column(db.Text, nullable=False)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
