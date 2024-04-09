from sqlalchemy import create_engine, MetaData, text
from pprint import pprint

engine = create_engine('sqlite:///technical_test.db', echo=True)
meta = MetaData()

connection = engine.raw_connection()
cursor = connection.cursor()

with engine.connect() as conn:
    
    # Test
    pprint(conn.execute(text(
        "SELECT code_postal_dept, count (*) as comptage FROM hotel group by code_postal_dept ORDER BY comptage DESC limit 5"))
           .fetchall())
    
    pprint(conn.execute(text(
        "SELECT code_postal_dept, classement,count (*) as comptage FROM hotel group by code_postal_dept, classement ORDER BY comptage DESC limit 5"))
           .fetchall())
    
    pprint(conn.execute(text(
        "SELECT code_postal_dept, classement,count (*) as comptage FROM hotel WHERE classement='5 étoiles' group by code_postal_dept, classement ORDER BY code_postal_dept"))
           .fetchall())