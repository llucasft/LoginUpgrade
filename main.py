import pyodbc

data_conn = (
    "Driver={SQL Server};"
    "Server=DESKTOP-G90E8IG\SQLSERVER;"
    "Database=all_data;"
    "Trusted_Connection=Yes"
)

conn = pyodbc.connect(data_conn)

cursor = conn.cursor()

command = """INSERT INTO usuarios(nome, nick, senha)
VALUES ('Ana Maria', 'anam', '456')"""

cursor.execute(command)
cursor.commit()
