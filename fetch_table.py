
from configparser import ConfigParser
import pymysql

def getTable(tableName, cols,keyID):
    
    configur = ConfigParser()
    configur.read('config.ini')  
    cnx = pymysql.connect(user=str(configur.get('secret','user')),
                        password=str(configur.get('secret','password')),
                        host=str(configur.get('secret','host')),
                        database=str(configur.get('secret','database')))
                                
    cursor = cnx.cursor()
    columns="t."+cols[0]
    for i in range(1,len(cols)):
        columns += ',t.'+cols[i]
    query = "SELECT {} FROM {} AS t".format(columns,tableName)
    # query = "SELECT t.eventid,t.title FROM event AS t"

    cursor.execute(query)

    ColHeader=""
    for i in range(0,len(cols)):
        ColHeader += '<th>'+cols[i]+'</th>'
    # Read data and generate code for a HTML table.
    print("<table border='1'><tr>{}</tr>".format(ColHeader))

    print("<h3>CSCI student info</h3>")
    for (eventid, title) in cursor:
        print("<tr><td>{}</td><td>{}</td></tr>".format(eventid, title))

    cursor.close()
    cnx.close()
    print ('''
    </table>
    </body>
    </html>
    ''')