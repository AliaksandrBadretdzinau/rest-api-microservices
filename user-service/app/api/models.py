from sqlmodel import Field, SQLModel, Relationship

from typing import Optional


class UserEmailLink(SQLModel, table=True):
    user_id: Optional[int] = Field(
        default=None, foreign_key='user.id', primary_key=True
    )
    email_id: Optional[int] = Field(
        default=None, foreign_key='email.id', primary_key=True
    )


class UserPhoneNumberLink(SQLModel, table=True):
    user_id: Optional[int] = Field(
        default=None, foreign_key='user.id', primary_key=True
    )
    phone_number_id: Optional[int] = Field(
        default=None, foreign_key='phonenumber.id', primary_key=True
    )


class UserBase(SQLModel):
    last_name: str = Field(index=True)
    first_name: str = Field(index=True)


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    emails: list['Email'] = Relationship(
        link_model=UserEmailLink,
    )

    phone_numbers: list['PhoneNumber'] = Relationship(
        link_model=UserPhoneNumberLink,
    )


class Email(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    mail: str = Field(index=True)


class PhoneNumber(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    number: str = Field(index=True)
