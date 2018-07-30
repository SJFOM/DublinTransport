import urllib2
import xml.etree.ElementTree as ET

stop = "phi" # Phibsborough stop abbreviation
#stop = "sti" # Stillorgan stop
contents = urllib2.urlopen(''.join(["https://luasforecasts.rpa.ie/xml/get.ashx?action=forecast&stop=",\
	stop,"&encrypt=false"])).read()

tree = ET.ElementTree(ET.fromstring(contents))
root = tree.getroot()

# print retrieved status message
print root.findall('message')[0].text
# print tram due times, their direction and their destinations
for direction in root.iter('direction'):
	print "\n" + direction.get('name')
	for tram in direction:
		dueMins = tram.get('dueMins')
		if(dueMins.lower() == 'DUE'.lower()):
			print "\tLuas to %s is due now!" % (tram.get('destination'))
		elif(dueMins.lower() == ''):
			print tram.get('destination')
		else:
			print "\tLuas to %s is due in %s minutes" % (tram.get('destination'), tram.get('dueMins'))

