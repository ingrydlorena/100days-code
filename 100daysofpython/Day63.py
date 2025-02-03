'''
Day 63: CRUD application
Build a basic CRUD (Create, Read, Update, Delete) application.
'''
import mysql.connector

connection = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '092632@In100' ,
    database= 'bd_day63',
)

cursor = connection.cursor()
'''
# CREATE
name_product = "Watch"
value = 17
command_create = f'INSERT INTO sells (Name_product, Value) VALUES ("{name_product}", {value})'
cursor.execute(command_create)
connection.commit()


# READ
command_read = 'SELECT * FROM sells'
cursor.execute(command_read)
result = cursor.fetchall()
print(result)


# UPDATE
name_product = "TV"
value_update = 1700
command_update = f'UPDATE sells SET Value = {value_update} WHERE Name_product = "{name_product}"'
cursor.execute(command_update)
connection.commit()


# DELETE
id_sells = 2
command_delete = f'DELETE FROM sells WHERE IDsells = "{id_sells}"'
cursor.execute(command_delete)
connection.commit()
'''

cursor.close()
connection.close()