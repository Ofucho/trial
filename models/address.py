from app import db

class Addresses(db.Model):
    __tablename__='address'

    id = db.Column(db.Integer,primary_key=True)
    national_id = db.Column(db.Integer,foreign_key=True)
    county = db.Column(db.String, nullable=False)
    subcounty = db.Column(db.VARCHAR, nullable=False)




    def add_records(self):
        db.session.add(self)
        db.session.commit()

        # Fetch all reords

    @classmethod
    def fetch_all_records(cls):
        return cls.query.all()
