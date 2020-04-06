import cx_Oracle

username = 'STUDENT1'
password = 'STUDENT1'
database = '192.169.1.105/orcl'


connection = cx_Oracle.connect(username,password,database)


query =""" SELECT 'Hello from Oracle!' FROM DUAL """

cursor = connection.cursor()


cursor.execute(query)

result = cursor.fetchone()[0]

print(result)

cursor.close()
connection.close()
