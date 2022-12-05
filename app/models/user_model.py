from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from app import db

class User(UserMixin, db.Model):
    # Table columns:
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True, unique=True, nullable=False)
    email = db.Column(db.String, index=True, unique=True, nullable=False)
    name = db.Column(db.String, index=True, unique=False, nullable=False)
    joined_at = db.Column(db.DateTime(), index=True, unique=False, nullable=False)
    password = db.Column(db.String)
    # Relationships: 
    # Implement accordingly with project nescessity
    
    # Class Methods
    def __init__(self, name:str, username:str, email:str, password:str) -> None:
        self.name = name
        self.username = username
        self.email = email
        self.set_password(passwd=password)
        self.joined_at = datetime.utcnow()
        
    
    def __repr__(self) -> str:
        return f"<id: {self.id} - username: {self.username} - joined at: {self.joined_at.date()}>"
    
    
    def set_password(self, passwd:str) -> None:
        '''
        Generate and store the hash from the given password.
        passwd: String, password
        '''
        self.password = generate_password_hash(password=passwd)
        
        
    def check_password(self, passwd:str) -> bool:
        '''
        Check if the hash of given password is equal to the stored hash.
        passwd: String, password
        '''
        return check_password_hash(pwhash=self.password, password=passwd)