from src.db_utils.base import Base, engine, Session

session = None


def persist(input_object):
    generate_schema()
    session.add(input_object)
    session.commit()


def open_session():
    global session
    session = Session()


def close_session():
    session.close()


def generate_schema():
    Base.metadata.create_all(engine)


def retrieve_all(input_object):
    return session.query(input_object).all()


