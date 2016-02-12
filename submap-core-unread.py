import socket,sys
try:
    script, t = sys.argv
except ValueError:
    print "Error: Please see basic usage in README.md"
    exit()
i = '''
Author: Colly
Version: Core - 1.0
'''
b = '''
Subdomain Finder
    By Colly
'''
ls = open('subs.txt').read().split()
def sc(hostname):
    for ho in ls:
        try:
            k = socket.gethostbyname(ho+"."+t)
            print ho+"."+t
            print socket.gethostbyname(ho+"."+t+"\n")
        except socket.gaierror:
            False
        except KeyboardInterrupt:
            print "\nScan interrupted by user."
            exit()
print b,i
try:
    sc(t)
except KeyboardInterrupt:
    print "\nScan interrupted by user."
    exit(3)