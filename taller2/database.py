import mysql.connector

DB_HOST = "localhost"
DB_USER = "root"       # ajusta credenciales
DB_PASSWORD = "PTGZU5XynS0ZhQrGWsqy"
DB_NAME = "tienda"

def get_connection():
    conexion = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conexion