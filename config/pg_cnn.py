import psycopg2

Facturacion_app = psycopg2.connect(
    dbname="Facturacion",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)