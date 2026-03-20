from .extensions import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# ------------------ USER MODEL ------------------

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    password_hash = db.Column(db.String(256), nullable=False)

    cps = db.relationship(
        "CP",
        backref="user",
        cascade="all, delete-orphan",
        lazy=True
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"

# ------------------ PLATFORM MODEL ------------------

class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    problems = db.relationship(
        "CP",
        backref="platform",
        lazy=True
    )

    def __repr__(self):
        return f"<Platform {self.name}>"

# ------------------ CP MODEL ------------------

class CP(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    ques_no = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    difficulty = db.Column(db.String(10), nullable=True)

    done_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    is_fav = db.Column(db.Boolean, default=False)
    is_completed = db.Column(db.Boolean, default=False)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    platform_id = db.Column(
        db.Integer,
        db.ForeignKey("platform.id"),
        nullable=False
    )

    __table_args__ = (
        db.UniqueConstraint("ques_no", "platform_id", "user_id"),
    )

    def __repr__(self):
        return f"<CP {self.ques_no}>"