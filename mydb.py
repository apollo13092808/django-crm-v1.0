import mysql.connector
from decouple import config

my_database = mysql.connector.connect(host=config('DB_HOST', default='localhost'),
                                      user=config('DB_USER', default='root'),
                                      password=config('DB_PASSWORD'))

# prepare a cursor object
cursor_obj = my_database.cursor()

# create a database
cursor_obj.execute("CREATE DATABASE django_crm CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")

print("Database created successfully")
