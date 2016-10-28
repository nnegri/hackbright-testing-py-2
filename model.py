from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    
    Game.query.delete()
    
    tr = Game(name = "Ticket to Ride", description = "a cross-country train adventures")
    pg = Game(name = "Power Grid", description = "supply the most cities with power" )
    al = Game(name="Amazing Labyrinth", description="move around the shifting paths of the labyrinth in a race to collect various treasures")
    pf = Game(name="Princes of Florence", description="attract artists and scholars trying to become the most prestigious family in Florence")
    ag = Game(name="Agricola", description="farmers sow, plow the fields, collect wood, and feed their families")


    db.session.add_all([tr, pg, al, pf, ag])
    db.session.commit()

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
 