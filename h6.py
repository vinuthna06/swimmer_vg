#!"C:\Users\USER\AppData\Local\Programs\Python\Python37-32\python.exe"
from fetchData import getContent
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

getContent(args)

print ('''
    </body>
    </html>
    ''')