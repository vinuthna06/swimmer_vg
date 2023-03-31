
def getMeetContent(cursor):
    query = "SELECT m.meetid, m.Title, v.Name venue FROM meet AS m LEFT JOIN venue AS v ON m.venueid = v.VenueId"
    cursor.execute(query)
    print("<h3>There are {} meets. Please select one.</h3>".format(cursor.rowcount))
    print("<ol>")
    for (meetid,title,venue) in cursor:
        print("<li><a href='./h6.py?mid={}'>{}</a>: at {}.</li>".format(meetid,title,venue))
    print("</ol>")

def getSpecificMeetContent(cursor,mid):
    query = "SELECT m.Title FROM meet AS m WHERE m.MeetId = {}".format(mid)
    cursor.execute(query)
    meet = cursor.fetchone()
    print("<h3>Meet #{}: {}</h3>".format(mid,meet[0]))
    query = "SELECT e.eventid, e.title, count(1) count FROM event AS e left join participation p on e.EventId = p.EventId WHERE e.MeetId = {} GROUP BY e.Title ORDER BY 2 desc".format(mid)
    cursor.execute(query)
    print("<ol>")
    for (eventid,title,count) in cursor:
        print("<li><a href='./h6.py?eid={}'>{}</a>: {} participants.</li>".format(eventid,title,count))
    print("</ol>")
