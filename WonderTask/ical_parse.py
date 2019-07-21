#!python
from icalendar import Calendar
import datetime
import requests
import sys
events=[]
now=(datetime.date.today())
try:
	url=sys.argv[1]
except IndexError:
	print("No URL given...")
	sys.exit()
try:
	cal = Calendar.from_ical(requests.get(url).text)
except:
	print("Can't fetch .ics file, sorry...")
	sys.exit()
for e in cal.walk('vevent'):
    delta=e.get('dtstart').dt-now
    event=[e.get('summary'),(delta.days)]
    events.append(event)
events.sort(key=lambda x:x[1])
for e in events:
	print('['+str(e[1])+' Days Until Due]  '+e[0])
