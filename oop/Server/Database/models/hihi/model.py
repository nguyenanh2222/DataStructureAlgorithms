from sqlalchemy import VARCHAR, Column, select

from oop.Server.Database.base import Base


class Hihi(Base):
    __tablename__ = "hihi1"
    haha = Column('haha',VARCHAR(100))


# select(Hihi)