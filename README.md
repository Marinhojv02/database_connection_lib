About
===

This is a Python library designed to connect to a PostgreSQL database using SQLAlchemy. 
The library is designed to be reusable across multiple applications that connect to a same postgresql database.

## Features

- Connect to a PostgreSQL database
- Manage SQLAlchemy sessions
- Define and use SQLAlchemy models

## Dependencies

- sqlalchemy
- psycopg2-binary

## Getting Started

### 1. Install database_connection_lib
```
    pip install git+https://github.com/Marinhojv02/teste-python-lib.git
```

### 2. import it on a new project and stablish the database connection
```
    from database_connection_lib.database import Database
    
    db = Database(user="usern", password="password", host="host", port=port, database="database")
    db.connect()
```

### 3. import the models and use the database
```
    session = db.get_session()
    user = session.query(UserModel).filter(UserModel.email == "johndoe@example.com").first()
    print(user)
```

### 4. close the session at the end
```
    session.close()
    db.close()
```