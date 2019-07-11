from src.db_utils.base import Base, engine, Session

session = None


def persist(input):
    generate_schema()
    session.add(input.type)
    session.add(input)

    session.commit()


def open_session():
    global session
    session = Session()


def close_session():
    session.close()


def generate_schema():
    Base.metadata.create_all(engine)


def retrieve_all(input):
    return session.query(input).all()


