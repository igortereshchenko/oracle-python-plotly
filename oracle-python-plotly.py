
import chart_studio
chart_studio.tools.set_credentials_file(username='tereshchenko.igor', api_key='1n8yuJXEUn51pPnR3ecW')
import plotly.graph_objects as go
import chart_studio.plotly as py
import cx_Oracle



username = 'STUDENT1'
password = 'STUDENT1'
database = '192.169.1.105/orcl'


connection = cx_Oracle.connect(username,password,database)


query =""" 

SELECT
    trim(customers.cust_name),
    NVL(count(orders.order_num),0)
FROM
    customers left
    JOIN orders ON customers.cust_id = orders.cust_id
    
GROUP BY
    customers.cust_id,customers.cust_name

"""

cursor = connection.cursor()

cursor.execute(query)

names = []
values = []
for data in cursor.fetchall():
    names.append(data[0])
    values.append(data[1])


bar = go.Bar(x = names, y =values)

py.plot([bar], auto_open= True, filename='oracle-data')

