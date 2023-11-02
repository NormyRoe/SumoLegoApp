import pymysql
from django.db import connections


def get_database_connection():
    
    # Use Django's database connection settings
    connection = connections['default']

    return connection

