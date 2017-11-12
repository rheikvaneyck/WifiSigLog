# Import library and create instance of REST client.
from Adafruit_IO import Client
import datetime

# Wifi dessen Signal aufgezeichnet werden soll
# Hier die eignene ESSID eingeben
ap_essid = "Lorelei" 
# MAC Addresse, um bei mehreren Access Points eindeutig zu sein
# Hier die MAC Adresse des eigenen AP eingeben
ap1_mac = "50:C7:BF:58:C8:60" 

aio = Client('Hier Dein Adafruit_IO API Schlüssel')

now = datetime.datetime.now()

with open('/tmp/wifisig.log','r') as f:
	for line in f:
		items = line.split(';')
		timestamp = items[0]	
		ap = items[1]
		essid = items[2]
		if((ap == ap1_mac) and (essid == ap_essid)):
			ts = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
			diff = int(now.strftime("%s")) - int(ts.strftime("%s"))
			if(diff<900):
				print "%s signals: %f" % (timestamp, float(items[3]))
				aio.send('LoreleiAP1', float(items[3]))
