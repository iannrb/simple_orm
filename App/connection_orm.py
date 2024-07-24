from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

password = quote_plus("")
# se você usa algum caractere especial na sua senha do postgres, você precisa escrever sua senha na variável password e passar a variável na URI abaixo
# postgresql://usuario:senha@host/databasename
DATABASE_URI = f""

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()