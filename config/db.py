from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import os

MYSQL_USER = 'root'
MYSQL_PASSWORD = 'password'
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'defaultdb'

#mysqlsh --sql --host=sfo1.clusters.zeabur.com --port=30777 --user=root --password=Y9UEFrxH14OgZ872K6TueyJjD53mts0Q --schema=zeabur
#URL_DATABASE = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
URL_DATABASE = os.getenv('URL_DATABASE', "mysql+pymysql://root:AdZLWyqhVAchoUSCRRdtJrrocuzbMdVh@crossover.proxy.rlwy.net:56860/railway")

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



def get_db() :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_all_tables():
    Base.metadata.create_all(bind=engine)

