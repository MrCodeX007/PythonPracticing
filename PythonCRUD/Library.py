import pyodbc

server = 'COSYSSERVER\SQLEXPRESS'
database = 'NexGenCoSysDBDev'
username = 'sa'
password = 'Kt2GLWShdLua3'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    with pyodbc.connect(connection_string) as connection:
        print('Connected to SQL Server')
        # Perform database operations here
except pyodbc.Error as e:
    print('Connection error:', str(e))



cursor = connection.cursor()

#Fetching the data from the database table
cursor.execute('Select * from MemMemberRegistration')
rows = cursor.fetchall()
for row in rows:
    print(row)

"""
#For inserting the data
insert_query = "insert into Books (Name, Price) Values (?,?)"
data = ('21 Lession of Life', '650')
cursor.execute(insert_query,data)
connection.commit()



#To update the data
update_query = "Update Books SET Price = ? where Id = ?"
new_value = '500'
condition_value = '1'
cursor.execute(update_query,(new_value,condition_value))
connection.commit()
print('Data updated successfully.')

#To delete the data
delete_query = 'Delete from Books where Id = ?'
condition_value1 = '3'
cursor.execute(delete_query,(condition_value1))
"""



