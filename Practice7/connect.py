import psycopg2
from config import db_host, db_database, db_user, db_password

def get_db_connection():
    return psycopg2.connect(
        host= db_host,
        database= db_database,
        user= db_user,
        password= db_password
    )