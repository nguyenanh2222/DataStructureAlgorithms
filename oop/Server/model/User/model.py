from datetime import datetime

from pydantic import BaseModel, Field


class TemplateLogin(BaseModel):
    username: str = Field(None)
    password: str = Field(None)


class UserReq(BaseModel):
    id: str = Field(None)
    uuid: str = Field(None)
    first_name: str = Field(None)
    middle_name: str = Field(None)
    last_name: str = Field(None)
    mobile: str = Field(None)
    email: str = Field(None)
    username: str = Field(None)
    registered_at: datetime = Field(None)
    last_login: datetime = Field(None)
    intro: str = Field(None)
    profile: str = Field(None)
    is_active: str = Field(None)
    is_reported: str = Field(None)
    is_blocked: str = Field(None)
    action: str = Field("login")
    status: bool = Field(True)


class AnonymusReq(BaseModel):
    action: str = Field("login")
    status: bool = Field(False)
