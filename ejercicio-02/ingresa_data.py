from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
from genera_base import Pais
import json

engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

archivo = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')

documentos =  archivo.json()


for d in documentos:
    p = Pais(nombre=d['CLDR display name'], 
            capital=d['Capital'],
            continente=d['Continent'],
            dial=d['Dial'],
            geonameId=d['Geoname ID'],
            itu=d['ITU'],
            lenguajes=d['Languages'],
            independiente=d['is_independent'],
        )
    session.add(p)

session.commit()
