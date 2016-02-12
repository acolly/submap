import socket
from sys import argv
try:
    script, target = argv
except ValueError:
    print "Error: Please specify a target using 'python submap.py [target]' by replacing" \
          " [target] with the desired url."
    exit()
# Define info
info = '''
Author: Colly
Version: Core - 1.0
'''
# Define the banner
banner = '''
Subdomain Finder
    By Colly
'''
# Make a list directly from the text file using .split()
listedsubdomains = open('subs.txt').read().split()
# Define the scan() function
def scan(hostname):
    for hostname in listedsubdomains:
        try:
            k = socket.gethostbyname(hostname+"."+target) # Try to gethostbyname without print to test if it works
            print hostname+"."+target # That way here we can print the url first
            print socket.gethostbyname(hostname+"."+target+"\n") # Actually print gethostbyname
        except socket.gaierror: # Handle it being an invalid subdomain
            False # Boolean filler
        except KeyboardInterrupt: # Handle the KeyboardInterrupt (Ctrl-C) separately
            print "\nScan interrupted by user."
            exit()
# Finally just run it
if __name__ == '__main__':
    print banner,info
    try:
        scan(target)
    except KeyboardInterrupt:
        print "\nScan interrupted by user."
        exit(3)