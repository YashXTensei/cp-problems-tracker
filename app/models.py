from .extensions import db
from datetime import datetime

class CP (db.Model) :
    id = db.Column(db.Integer , primary_key = True)
    platform = db.Column(db.String(100) , default = "CodeForces")
    ques_no = db.Column(db.String(100) , nullable = False)
    rating = db.Column(db.String(100) , default = "800")
    done_at = db.Column(db.DateTime , default = datetime.utcnow)
    is_fav = db.Column(db.Boolean , default = False)
    is_completed = db.Column(db.Boolean , default = False)

    def __repr__(self):
        return f"<CP {self.ques_no}>"