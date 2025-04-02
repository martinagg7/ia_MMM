#Librerias
import pyodbc
import pandas as pd
import os

# Carpeta para guardar en formato CSV las tablas que nos cargemos de azure
os.makedirs("data/raw", exist_ok=True)

# Parámetros de conexión
server = 'uaxmathfis.database.windows.net'
database = 'usecases'
driver = '{ODBC Driver 18 for SQL Server}'

conn_str = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Authentication=ActiveDirectoryInteractive'
)

conn = pyodbc.connect(conn_str)

# Tablas
tablas = {
    'MMM01_WEB': 'web',
    'MMM02_VISIT': 'visit',
    'MMM03_OFFLINE': 'offline',
    'MMM04_TIME': 'time',
    'MMM05_INV': 'inv'
}

# Cargar y guardar las tablas
for nombre_sql, nombre_archivo in tablas.items():
    print(f"Cargando tabla: {nombre_sql}")
    df = pd.read_sql(f"SELECT * FROM DATAEX.{nombre_sql}", conn)
    df.to_csv(f"data/raw/{nombre_archivo}.csv", index=False)
    print(f"Guardada en: data/raw/{nombre_archivo}.csv")

print("Las tablas han sido cargadas y guardadas correctamente")
