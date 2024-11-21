### create environment

    py -3 -m venv .env

### Activate venv
    .env/Scripts/activate


### Install Flask and other dependencies using `pip`

   `pip install flask flask-restful flask-sqlalchemy flask-migrate python-dotenv`

### Database Migration Commands

    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
