from app import db

class Owner(db.Model):
    __tablename__='owner'

    id = db.Column(db.Integer,unique=True,nullable=False)
    national_id = db.Column(db.String, primary_key=True,unique=True,nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    addresses=db.relationship('Addresses', backref='owner', lazy=True)

class Addresses(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    national_id = db.Column(db.String, db.ForeignKey('owner.national_id'), nullable=False)
    county = db.Column(db.String, nullable=False)
    subcounty = db.Column(db.String, nullable=False)



    def add_records(self):
        db.session.add(self)
        db.session.commit()

        # Fetch all reords

    @classmethod
    def fetch_all_records(cls):
        return cls.query.all()

    def fetch_by_id(self):
        return self.id