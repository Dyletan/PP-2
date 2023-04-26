import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="pp2",
    user="postgres",
    password="pass")