
from configparser import ConfigParser
import pymysql
from meet import getMeetContent,getSpecificMeetContent
from event import getEventContent

def getContent(args):
    
    configur = ConfigParser()
    configur.read('config.ini')  
    cnx = pymysql.connect(user=str(configur.get('secret','user')),
                        password=str(configur.get('secret','password')),
                        host=str(configur.get('secret','host')),
                        database=str(configur.get('secret','database')))
                                
    cursor = cnx.cursor()
    # print(args)
    if "mid" not in args and "eid" not in args:
        getMeetContent(cursor)
    elif "mid" in args:
        getSpecificMeetContent(cursor,args['mid'][0])
    elif "eid" in args:
        getEventContent(cursor,args['eid'][0])

    cursor.close()
    cnx.close()