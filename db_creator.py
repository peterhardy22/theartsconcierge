from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# connects Python to the database
engine = create_engine('sqlite:///artworks.db', echo=True)
# Class that we can use to create declarative class definitions
# that actually define our database tables
Base = declarative_base()


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Artist: {}>".format(self.name)


class Artwork(Base):
    __tablename__ = "artworks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    medium = Column(String)
    dimensions = Column(String)
    image = Column(String)
    location = Column(String)
    city = Column(String)
    country = Column(String)
    latitude = Column(Integer)
    longitude = Column(Integer)
    on_view = Column(Boolean, default=False)

    artist_id = Column(Integer, ForeignKey("artists.id"))
    artist = relationship("Artist", backref=backref(
        "artworks", order_by=id))


# Create tables
Base.metadata.create_all(engine)
