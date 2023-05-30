from sqlmodel import Session, select

from .db import engine
from .models import User, Email, PhoneNumber
from .schemas import UserCreate


def get_user(user_id: int):
    with Session(engine) as session:
        user = session.exec(
            select(User).where(User.id==user_id)
        ).one_or_none()

        return user and {
            **user.dict(),
            'emails': user.emails,
            'phone_numbers': user.phone_numbers
        }


def get_users(field: str = None, value: any = None):
    with Session(engine) as session:
        is_field_enabled = field and value

        base_selector = select(User)
        query = base_selector.where(
            getattr(User, field)==value
        ) if is_field_enabled else base_selector
        users = session.exec(query).all()
        
        return [
            {
                **user.dict(),
                'emails': user.emails,
                'phone_numbers': user.phone_numbers
            }
            for user in users
        ]


def create_user(payload: UserCreate):
    with Session(engine) as session:
        user = User(**dict(payload))

        session.add(user)
        session.commit()
        session.refresh(user)

        return {
            **user.dict(),
            'emails': user.emails,
            'phone_numbers': user.phone_numbers
        }


def add_email(user_id: int, email: Email):
    with Session(engine) as session:
        user = session.exec(
            select(User).where(User.id==user_id)
        ).one()
        user.emails.append(email)
        session.add(user)
        session.commit()

        return {
            'user_id': user.id,
            'emails': user.emails
        }


def update_email(email_id: int, email: Email) -> Email | None:
    with Session(engine) as session:
        db_email = session.exec(
            select(Email).where(Email.id==email_id)
        ).one_or_none()
        
        if not db_email:
            return None
        
        db_email.mail = email.mail
        session.add(db_email)
        session.commit()
        session.refresh(db_email)

        return db_email.dict()


def add_phone_number(user_id: int, phone_number: PhoneNumber):
    with Session(engine) as session:
        user = session.exec(
            select(User).where(User.id==user_id)
        ).one()
        user.phone_numbers.append(phone_number)
        session.add(user)
        session.commit()

        return {
            'user_id': user.id,
            'phone_numbers': user.phone_numbers
        }


def update_phone_number(
    phone_number_id: int,
    phone_number: PhoneNumber
) -> PhoneNumber | None:
    with Session(engine) as session:
        db_phone_number = session.exec(
            select(PhoneNumber).where(PhoneNumber.id==phone_number_id)
        ).one_or_none()
        
        if not db_phone_number:
            return None
        
        db_phone_number.number = phone_number.number
        session.add(db_phone_number)
        session.commit()
        session.refresh(db_phone_number)

        return db_phone_number.dict()


def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.exec(
            select(User).where(User.id==user_id)
        ).one()
        session.delete(user)
        session.commit()
