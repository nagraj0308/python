import mysql.connector
connection=mysql.connector.connect(user='root',password='@nagendra',host='localhost',database='python')
mycursor=connection.cursor()
mycursor.execute("select * from python")
tab=mycursor.fetchall()
for tu in tab:
	print(tu[0],tu[1],tu[2])



