import socket
from sys import argv
'''
TODO: - Use argpparse instead of argv
      - Actually make dns requests
'''
try:
    script, target = argv
except ValueError:
    print "Error: Please specify a target using 'python submap.py [target]' by replacing" \
          "[target] with the desired url."
    exit()

# Define info
info = '''
Author: Colly
Version: 1.0
'''

# Define the banner
banner = '''
   _____       _         _                       _         ______ _           _
  / ____|     | |       | |                     (_)       |  ____(_)         | |
 | (___  _   _| |__   __| | ___  _ __ ___   __ _ _ _ __   | |__   _ _ __   __| | ___ _ __
  \___ \| | | | '_ \ / _` |/ _ \| '_ ` _ \ / _` | | '_ \  |  __| | | '_ \ / _` |/ _ \ '__|
  ____) | |_| | |_) | (_| | (_) | | | | | | (_| | | | | | | |    | | | | | (_| |  __/ |
 |_____/ \__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_| |_|    |_|_| |_|\__,_|\___|_|
'''

# Make a list directly from the text file using .split()
listedsubdomains = open('subs.txt').read().split()

# Define the scan() function
def scan(hostname):
    for hostname in listedsubdomains:
        try:
            socket.gethostbyname(hostname+"."+target) # Try to gethostbyname without print
                                                      # to test if it works
            print hostname+"."+target+"\n" # That way here we can print the url first
            print socket.gethostbyname(hostname+"."+target) # Actually print gethostbyname
        except socket.gaierror: # Handle it being an invalid subdomain
            hostname = False # Just do something to avoid more errors
        except KeyboardInterrupt as error: # Handle the KeyboardInterrupt separately
            print "\nScan interrupted by user."
            error = error
            exit()
        except:
            print "Unknown error. Please include the console log in your bug" \
                  " report."

# Define the intro() function
def intro():
    print banner,info

# Finally just run it
if __name__ == '__main__':
    intro()
    scan(target)