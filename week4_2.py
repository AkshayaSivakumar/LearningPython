import urllib
import json

service_url = "http://python-data.dr-chuck.net/geojson?"

while True:
	location = raw_input("Enter location: ")
	if len(location) < 1: break
	
	urlToFetch = service_url + "?" + urllib.urlencode({'sensor':'false', 'address':location})
	print "Retrieving ", urlToFetch
	data = urllib.urlopen(urlToFetch).read()
	print "Retrieved ", len(data), " characters"
	
	info = json.loads(data)
	
	pid = info["results"][0]["place_id"]
	print "Place id ", pid