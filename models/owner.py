from app import db

class Owner(db.Model):
    __tablename__='owner'

    national_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.VARCHAR, nullable=False)

    def add_records(self):
        db.session.add(self)
        db.session.commit()

        # Fetch all reords

    @classmethod
    def fetch_all_records(cls):
        return cls.query.all()
