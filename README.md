# Online Store

## Description

This is a simple online store built with Python and Flask.

## Requirements

-   Python 3.x
-   Flask
-   Flask-SQLAlchemy
-   Flask-Login
-   Flask-WTF

## Installation

### 1. Create a virtual environment:

```bash
python -m venv .venv
```

### 2. Install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Copy the `.env.example` file to `.env` and fill in the necessary environment variables:

```bash
cp .env.example .env
```

### 4. Configure environment variables:

Generate a secret key for your application:

```bash
python -c 'import secrets; print(secrets.token_hex())'

```

```
# Database SQLite

SECRET_KEY=your_secret_key # paste the generated secret key
SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3
SQLALCHEMY_TRACK_MODIFICATIONS=False

# Change to True for development mode and False for production mode
FLASK_DEBUG=False
FLASK_ENV=production

# User Admin
USER_ADMIN_USERNAME=admin
USER_ADMIN_PASSWORD=admin
USER_ADMIN_EMAIL=admin@gmail.com
```

### 5. Initialize migrations:

```bash
flask db init
```

### 6. Run the application:

```bash
flask run
```

## Usage

To access the application, open your web browser and navigate to `http://localhost:5000/`.
