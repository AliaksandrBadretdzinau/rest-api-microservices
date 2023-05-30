from fastapi import APIRouter, HTTPException, status, Response

from .db import engine
from ..api import db_manager
from .models import User, Email, PhoneNumber
from .schemas import UserCreate, UserRead, UserEmailsRead, Userphone_numbersRead

users = APIRouter(
    prefix="/users",
    tags=["users"]
)

@users.get(
    "/{user_id}",
    response_model=UserRead
)
def get_user(user_id: int):
    user = db_manager.get_user(user_id=user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


@users.get('/', response_model=list[UserRead])
def get_users(response: Response, field: str = None, value: str = None):
    if field and field not in User.schema()['properties']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Wrong field provided"
        )

    if field and not value:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Value has to be provided"
        )
    
    users = db_manager.get_users(field=field, value=value)

    if not users:
        response.status_code=status.HTTP_204_NO_CONTENT

    return users


@users.post(
    "/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED
)
def create_user(payload: UserCreate):
    user = db_manager.create_user(payload=payload)

    return user


@users.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(user_id: int):
    db_manager.delete_user(user_id=user_id)


@users.post(
    "/{user_id}/emails",
    response_model=UserEmailsRead,
    status_code=status.HTTP_201_CREATED
)
def add_email(user_id: int, payload: Email):
    emails = db_manager.add_email(user_id=user_id, email=payload)

    return emails


@users.put(
    "/{user_id}/emails/{email_id}",
    response_model=Email
)
def update_email(user_id: int, email_id: int, payload: Email):
    email = db_manager.update_email(email_id=email_id, email=payload)

    if not email:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email not found"
        )
    
    return email


@users.post(
    "/{user_id}/phone-numbers",
    response_model=Userphone_numbersRead,
    status_code=status.HTTP_201_CREATED
)
def add_phone_number(user_id: int, payload: PhoneNumber):
    phone_numbers = db_manager.add_phone_number(user_id=user_id, phone_number=payload)

    return phone_numbers


@users.put(
    "/{user_id}/phone-numbers/{phone_number_id}",
    response_model=PhoneNumber
)
def update_phone_number(user_id: int, phone_number_id: int, payload: PhoneNumber):
    phone_number = db_manager.update_phone_number(phone_number_id=phone_number_id, phone_number=payload)

    if not phone_number:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Phone number not found"
        )
    
    return phone_number
