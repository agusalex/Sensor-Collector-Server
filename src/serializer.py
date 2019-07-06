from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB connection
engine = create_engine('sqlite:///../data/triangulation.db', echo=True)
# Session factory
Session = sessionmaker(bind=engine)
Base = declarative_base()


# Declare mapping
class TestObject(Base):
    __tablename__ = 'testobjects'

    mac = Column(String, primary_key=True)
    decib = Column(Integer)

    def __repr__(self):
        return "<testObject(mac='%s', db='%i')>" % (
            self.mac, self.decib)


# Create schemas
Base.metadata.create_all(engine)


# Start session
session = Session()

asd = TestObject(mac='8C-A5-E3-D2-C9-85', decib=14)

# Persist object
session.add(asd)
# Commit transaction
session.commit()

# Execute query
traidos = session.query(TestObject).all()
for traido in traidos:
    print('*****************************************' + str(traido))

# Close session
session.close()
