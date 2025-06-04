from main import db
from sqlalchemy.sql import func

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())