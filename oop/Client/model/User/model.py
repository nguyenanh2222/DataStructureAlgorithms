from datetime import datetime

import orjson
from pydantic import BaseModel, Field


class UserLogin(BaseModel):
    username: str = Field(None)
    password: str = Field(None)
    event: str = Field("Login")


class User(BaseModel):
    id: str = Field(None)
    uuid: str = Field(None)
    first_name: str = Field(None)
    middle_name: str = Field(None)
    last_name: str = Field(None)
    username: str = Field(...)
    password_hash: str = Field(None)
    password: str = Field(...)
    mobile: str = Field(None)
    email: str = Field(None)
    registered_at: datetime = Field(None)
    last_login: datetime = Field(None)
    intro: str = Field(None)
    profile: str = Field(None)
    is_active: bool = Field(None)
    is_reported: bool = Field(None)
    is_blocked: bool = Field(None)



