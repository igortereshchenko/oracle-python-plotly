import cx_Oracle

username = 'STUDENT1'
password = 'STUDENT1'
database = '192.169.1.105/orcl'


connection = cx_Oracle.connect(username,password,database)
cursor = connection.cursor()


query="""

select 
        cust_name, 
        cust_id 
    from customers 
    where trim(cust_country) = :country

"""

cursor.execute(query, country='USA')

for record in cursor.fetchall():
    print(record)


cursor.close()
connection.close()

