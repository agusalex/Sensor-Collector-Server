from src.db_utils.base import Base, engine, Session


def persist(input):
    # 2 - generate database schema
    Base.metadata.create_all(engine)

    # 3 - create a new session
    session = Session()

    session.add(input)

    session.commit()
    session.close()
