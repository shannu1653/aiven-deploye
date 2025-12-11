import pymysql
pymysql.install_as_MySQLdb()

from django.db.backends.mysql.base import (
    DatabaseWrapper as DjangoMySQLDatabaseWrapper,
)

class DatabaseWrapper(DjangoMySQLDatabaseWrapper):
    pass
