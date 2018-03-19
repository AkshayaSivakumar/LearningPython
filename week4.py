import urllib
import json

urlToOpen = raw_input("Enter location: ")
print "Retrieving ", urlToOpen
data = urllib.urlopen(urlToOpen).read()
print "Retrieved ", len(data)," characters"
info = json.loads(data)
total = 0
print "Count: ", len(info['comments'])
for i in range(0, len(info['comments'])):  
    total += int(info['comments'][i]['count'])  
print "Sum ", total

