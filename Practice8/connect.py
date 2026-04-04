import psycopg2
from config import db_host, db_name, db_user, db_password

def get_db_connection():
    return psycopg2.connect(
        host=db_host,
        dbname=db_name,
        user=db_user,
        password=db_password
    )