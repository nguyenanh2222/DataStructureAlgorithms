from sqlalchemy import Column, VARCHAR, DateTime, TEXT
from sqlalchemy.dialects.mysql import TINYTEXT, BIGINT, TINYINT

from oop.Server.Database.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column("id", BIGINT(20), primary_key=True)
    uuid = Column("uuid", VARCHAR(26), comment="UUID")
    first_name = Column("firstName", VARCHAR(50), comment="firstName")
    middle_name = Column("middleName", VARCHAR(50), comment="middleName")
    last_name = Column("lastName", VARCHAR(50), comment="lastName")
    username = Column("username", VARCHAR(50), comment="username")
    password_hash = Column("passwordHash", VARCHAR(32), comment="passwordHash")
    password = Column("password", VARCHAR(100), comment="username")
    mobile = Column("mobile", VARCHAR(32), comment="mobile")
    email = Column("email", VARCHAR(50), comment="email")
    registered_at = Column("registeredAt", DateTime, comment="registered_at")
    last_login = Column("last_login", DateTime, comment="last_login")
    intro = Column("intro", TINYTEXT, comment="intro")
    profile = Column("profile", TEXT, comment="profile")
    is_active = Column("is_active", TINYINT(1), comment="is_active")
    is_reported = Column("is_reported", TINYINT(1), comment="is_reported")
    is_blocked = Column("is_blocked", TINYINT(1), comment="is_blocked")
