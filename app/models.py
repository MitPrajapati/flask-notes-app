from app import db
from datetime import datetime,UTC

class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable = False)
    content = db.Column(db.Text,nullable = False)
    created_at = db.Column(db.DateTime,default= lambda:datetime.now(UTC))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = False)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),unique=True,nullable=False)
    email = db.Column(db.String(100),unique=True,nullable= False)
    password = db.Column(db.String(255),nullable=False)
