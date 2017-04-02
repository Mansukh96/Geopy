import time
from geopy.geocoders import Nominatim
f = open("kash.txt","r")
geolocator = Nominatim()
kash = ""
i = 0
for s in f.readlines():
	if i % 20 == 0:
		time.sleep(2)
	i = i + 1
	kash = s.strip()	
	location = geolocator.geocode(kash+",Kashmir,India")
        if location is not None:
		print((kash,location.latitude,location.longitude))
		
