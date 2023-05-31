# User service

This serice represents REST API which is able to:

- Create new user with contact data
- Return user by id
- Return user by name
- Add additional mail/phone data
- Update existing mail/phone data
- Delete user

## Tech Stack

- Runtime: Python 3.11
- Framework: FastAPI
- ORM: SqlModel
- Validation: Pydantic behild SqlModel
- DB: Sqlite3
- Documentation: Swagger

## Models

```
User:
    id: <int>
    lastName: <string>
    firstName: <string>
    emails: List<Email>
    phoneNumbers: List<PhoneNumber>

Email:
    id: <int>
    mail: <string>
    
PhoneNumber:
    id: <int>
    number: <string>
```

## API documention

Once you run the project you can find API documentation based on Swagger UI here: (Done automatically by FastAPI)

`http://0.0.0.0:8080/users/docs`
