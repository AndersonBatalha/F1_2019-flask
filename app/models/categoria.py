from app import db

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id_categoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cat = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.cat