from .models import UserBase, Email, PhoneNumber

from pydantic import BaseModel


class UserCreate(UserBase):
    emails: list[Email]
    phone_numbers: list[PhoneNumber]


class UserRead(UserBase):
    id: int
    emails: list[Email]
    phone_numbers: list[PhoneNumber]


class UserEmailsRead(BaseModel):
    user_id: int
    emails: list[Email]


class UserPhoneNumberRead(BaseModel):
    user_id: int
    phone_numbers: list[PhoneNumber]
