def getEventContent(cursor,eid):
    print("<h3>Participants in Event# {}</h3>".format(eid))
    query = "SELECT s.LName,s.FName ,s.Phone FROM `participation` as p left join swimmer as s on p.SwimmerId = s.SwimmerId WHERE p.EventId = {}".format(eid)
    cursor.execute(query)
    print("<ol>")
    for (lname,fname,phone) in cursor:
        print("<li>{} {}: {}</li>".format(lname,fname,phone))
    print("</ol>")

    