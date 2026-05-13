import sqlite3
pytosql = sqlite3.connect("gastos.db")
cursor = pytosql.cursor()
#conexāo python a sql

cursor.execute("""
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preço_und REAL NOT NULL,
    total REAL NOT NULL,
    data DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
pytosql.commit()

def leide(i,c,p,t):
 cursor.execute("INSERT INTO compras (item,quantidade,preço_und,total) VALUES(?,?,?,?)",
 (i,c,p,t))
 pytosql.commit()
def historico():
 print("\n--Historico De Compras--")
 cursor.execute("SELECT * FROM compras")
 datos = cursor.fetchall()
 for fila in datos:
  print(f"#{fila[0]}  - {fila[1]} | Cant:{fila[2]} | Preço_und:{fila[3]} | Total: {fila[4]} | Fecha: {fila[5]}")     


while True:
 print ("Bem-Vindo A Caixa Registradora\n")
 print ("Seleccione uma opçāo\n")
 print ("""
 1.Registrar Vendas
 2.Historico
 3.Sair""")

 opcion = int(input(""))
 if opcion == 1:
  while True:
   item = input("Item: ")
   cantidad = int(input("Quantidade: "))
   precio = float(input("Preço unidade: "))
   total = cantidad * precio
   print("Total: ", total)
   leide(item,cantidad,precio,total)
   print("Sucesso!\n")
   print("1.Nova compra 2.sair")
   opcion2 = int(input(""))
   if opcion2 == 2:
    print("saindo...")
    break
   else:
    print("Nova Compra")
 elif opcion == 2:
  historico()

  print("\n1.Voltar 2.Editar 3.Apagar")
  opcion3 = int(input(""))
  if opcion3 == 2:
   print("Digite o ID do Item a Editar\n")
   opcion4 = int(input(""))

   print("Seleccione A Informaçāo A Editar\n")
   print("""
   1.Item
   2.Quantidade
   3.Preço_und
   4.Total
   5.data
   """)
   opcion5 = int(input(""))
   if opcion5 == 1:
    print("-Atualizar Nome Do Item-")
    op5_1 = input(" ")
    cursor.execute("UPDATE compras SET item = ? WHERE id =?",(op5_1,opcion4))

    print("Sucesso!")
   elif opcion5 == 2:
    print("-Atualizar Quantidade-")
    op5_2 = int(input(""))
    cursor.execute("UPDATE compras SET quantidade = ? WHERE id =?",(op5_2,opcion4))

    print("Sucesso!")
   elif opcion5 == 3:
    print("-Atualizar Preço_Unidade-")
    op5_3 = float(input(" "))
    cursor.execute("UPDATE compras SET preço_und = ? WHERE id =?",(op5_3,opcion4))

    print("Sucesso!")
   elif opcion5 == 4:
    print("-Atualizar Total-")
    op5_4 = float(input(" "))
    cursor.execute("UPDATE compras SET total = ? WHERE id =?",(op5_4,opcion4))

    print("Sucesso!")
    
   elif opcion5 == 5:
    print("-Atualizar Data-") 
    op5_5 = input(" ")
    cursor.execute("UPDATE compras SET data = ? WHERE id =?",(op5_5,opcion4))

    print("Sucesso!") 
  elif opcion3 == 3:
   print("Digite o ID do Item a Apagar\n")
   opcion6 = int(input(""))
   cursor.execute("DELETE FROM compras WHERE id = ?",(opcion6,))
   print("Apagado Com Sucesso.")
   pytosql.commit()



   

 elif opcion == 3:
  print("Saindo...")
  break
