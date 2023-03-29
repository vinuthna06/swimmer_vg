#!"C:\Users\USER\AppData\Local\Programs\Python\\Python39\python.exe"
from dbconfig import *
import pymysql
# cgi: Support module for Common Gateway Interface (CGI) scripts.
# cgitb: Traceback manager for CGI scripts
# cgitb.enable(): enable trace back feature
import cgi
import cgitb
cgitb.enable()

#   Establish a cursor for MySQL connection.
db = get_mysql_param()
cnx = pymysql.connect(user=db['user'],
                      password=db['password'],
                      host=db['host'],
                      # port needed only if it is not the default number, 3306.
                      # port = int(db['port']),
                      database=db['database'])
                             
cursor = cnx.cursor()

#   Create HTTP response header
print("Content-Type: text/html;charset=utf-8")
print()

#   Create a primitive HTML starter
print ('''<html>
<head></head>
<body>
''')


query = '''
SELECT DISTINCT s.stuId,
    CONCAT(s.fname, ' ', s.lname) AS student,
    s.ach,
    IFNULL(CONCAT(f.fname, ' ', f.lname), 'N/A') AS advisor
FROM student AS s LEFT JOIN faculty AS f ON (s.advisor = f.facId)
WHERE s.major = 'CSCI'   
'''

cursor.execute(query)

# Read data and generate code for a HTML table.
print('''
<table border='1'>
<tr><th>Student Id</th><th>Name</th><th>Accumulated credits</th><th>advisor</th></tr>
''')

print("<h3>CSCI student info</h3>")
for (stuId, student, credits, advisor) in cursor:
    print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(stuId, student, credits, advisor))

cursor.close()
cnx.close()

print ('''
</table>
</body>
</html>
''')