#!"C:\Users\USER\AppData\Local\Programs\Python\Python37-32\python.exe"
from fetch_table import getTable
# cgi: Support module for Common Gateway Interface (CGI) scripts.
# cgitb: Traceback manager for CGI scripts
# cgitb.enable(): enable trace back feature
import cgi
import cgitb
cgitb.enable()
args = cgi.parse()


#   Establish a cursor for MySQL connection.
# db = get_mysql_param()

#   Create HTTP response header
print("Content-Type: text/html;charset=utf-8")
print()

#   Create a primitive HTML starter
print ('''<html>
<head></head>
<body>
''')
# print ("Port Server : ", configur.get('secret','database'))
# print("<h3>{}</h3>".format(args['x'][0]))
getTable("event",['eventid','title'],0)
