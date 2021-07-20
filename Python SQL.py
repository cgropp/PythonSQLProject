import mysql.connector

db = mysql.connector.connect(host="localhost",    
							user="PythonDBUser",         
							passwd="PythonDBPass",  
							db="invoicing")


testSelectQuery = "SELECT * FROM clients WHERE client_id > 1;"

with db.cursor() as cursor:
	cursor.execute(testSelectQuery)
	result = cursor.fetchall()
	for row in result:
		print(row)
	cursor.close()


db.close()