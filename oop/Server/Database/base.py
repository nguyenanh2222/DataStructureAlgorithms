from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session, DeclarativeMeta, declared_attr, as_declarative, declarative_base

from sqlalchemy.pool import QueuePool

engine = create_engine("mysql+pymysql://sang:123@localhost:3306/social_media", poolclass=QueuePool, pool_size=100,
                       max_overflow=-1, pool_recycle=3600)
session_factory = sessionmaker(engine)


def get_session() -> Session:
    """Provide a transactional scope around a series of operations."""
    session = session_factory()
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.commit()
        session.close()

def auto_commit(session : Session):
    print(session)
    session.commit()
    session.close()

# @as_declarative(metadata=MetaData(schema="social_media"))
@declarative_base
class Base:
    __name__: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def __str__(self):
        return str(self.__dict__)
