from pydantic import BaseModel, Field


class UserLogin(BaseModel):
    username: str = Field(None)
    password: str = Field(None)


class User(BaseModel):
    id = Field(None)
    uuid = Field(None)
    first_name = Field(None)
    middle_name = Field(None)
    last_name = Field(None)
    username = Field(...)
    password_hash = Field(None)
    password = Field(...)
    mobile = Field(None)
    email = Field(None)
    registered_at = Field(None)
    last_login = Field(None)
    intro = Field(None)
    profile = Field(None)
    is_active = Field(None)
    is_reported = Field(None)
    is_blocked = Field(None)

