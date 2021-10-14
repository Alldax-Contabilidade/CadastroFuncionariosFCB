import pyodbc

banco = pyodbc.connect('DSN=Contabil')
cursor = banco.cursor()

cursor.tables()
rows = cursor.fetchall()
# for row in rows:
 #   print(row.table_name)

cursor.execute(
    "SELECT * FROM externo.bethadba.foempregados WHERE codi_emp = 221"
)
tabela = cursor.fetchall()
print(tabela)
