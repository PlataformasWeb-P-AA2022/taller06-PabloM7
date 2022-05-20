from sqlalchemy import create_engine
engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'paises'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    capital = Column(String(100))
    continente = Column(String(100))
    dial = Column(String(100))
    geoname = Column(Integer)
    itu = Column(String(100))
    lenguajes = Column(String(100))
    independiente = Column(String(100))

    def __repr__(self):
        return "Pais: nombre=%s capital=%s continente:%s dial:%s itu:%s geonameId:%s lenguajes:%s independiente:%s" % (
                          self.nombre,
                          self.capital,
                          self.continente,
                          self.dial,
                          self.geoname,
                          self.itu,
                          self.lenguajes,
                          self.independiente)  

Base.metadata.create_all(engine)