from typing import Optional

from sqlalchemy import select

from oop.Server.Database.base import get_session, auto_commit
from oop.Server.Database.models.user.model import User


# @get_session
def login(username, password) -> Optional[User]:
    session = next(get_session())
    return session.query(User).filter(
        User.username == username,
        User.password == password,
    ).first()
