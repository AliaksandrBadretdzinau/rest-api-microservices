from fastapi.testclient import TestClient
from unittest import TestCase

from ...main import app, create_db_and_tables
from ...api.schemas import UserCreate
from ...api import db_manager
from ...api.models import Email, PhoneNumber
from ..utils.utils import get_email, get_phone_number, get_string

client = TestClient(app)

create_db_and_tables()

test_user = UserCreate(**{
    'last_name': get_string(),
    'first_name': get_string(),
    'emails': [
        {'mail': get_email()},
        {'mail': get_email()},
    ],
    'phone_numbers': [
        {'number': get_phone_number()},
        {'number': get_phone_number()},
    ]
})

def test_create_user() -> None:
    user_in = db_manager.create_user(payload=test_user)

    TestCase().assertDictEqual(
        {
            'id': user_in['id'],
            **test_user.dict()
        },
        user_in
    )


def test_get_users() -> None:
    users = db_manager.get_users()

    assert len(users) == 1

    first_user, *_ = users
    
    TestCase().assertDictEqual(
        {'id': first_user['id'],**test_user.dict()},
        first_user
    )


def test_get_user_by_id() -> None:
    first_user, *_ = db_manager.get_users()
    user = db_manager.get_user(first_user['id'])

    TestCase().assertDictEqual(
        {
            'id': first_user['id'],
            **test_user.dict()
        },
        user
    )


def test_get_user_by_last_name() -> None:
    first_user, *_ = db_manager.get_users()
    user, *_ = db_manager.get_users(field='last_name', value=test_user.last_name)

    TestCase().assertDictEqual(
        {
            'id': first_user['id'],
            **test_user.dict()
        },
        user
    )


def test_add_email() -> None:
    test_email = Email(mail=get_email())
    
    first_user, *_ = db_manager.get_users()
    result = db_manager.add_email(
        user_id=first_user['id'],
        email=test_email
    )
    *_, new_email = result['emails']

    assert len(result['emails']) == len(first_user['emails']) + 1
    assert result['user_id'] == first_user['id']
    assert new_email.mail == test_email.mail


def test_add_phone_number() -> None:
    test_phone_number = PhoneNumber(number=get_phone_number())

    first_user, *_ = db_manager.get_users()
    result = db_manager.add_phone_number(
        user_id=first_user['id'],
        phone_number=test_phone_number
    )
    *_, new_phone_number = result['phone_numbers']

    assert len(result['phone_numbers']) == len(first_user['phone_numbers']) + 1
    assert result['user_id'] == first_user['id']
    assert new_phone_number.number == test_phone_number.number


def test_update_email() -> None:
    first_user, *_ = db_manager.get_users()
    email, *_ = first_user['emails']
    email.mail = get_email()
    db_email = db_manager.update_email(email_id=email.id, email=email)

    TestCase().assertDictEqual(email.dict(), db_email)


def test_update_phone_number() -> None:
    first_user, *_ = db_manager.get_users()
    phone_number, *_ = first_user['phone_numbers']
    phone_number.number = get_phone_number()
    db_phone_number = db_manager.update_phone_number(
        phone_number_id=phone_number.id,
        phone_number=phone_number
    )

    TestCase().assertDictEqual(phone_number.dict(), db_phone_number)


def test_delete_user() -> None:
    first_user, *_ = db_manager.get_users()
    db_manager.delete_user(user_id=first_user['id'])
    user = db_manager.get_user(first_user['id'])

    assert user is None
