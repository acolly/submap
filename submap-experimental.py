from sys import argv
import socket
try:
    import dns.resolver
except ImportError: # This is the error given if dnspython isn't intalled
    print "[*] Please install dnspython first. Refer to the readme for more information."
    exit(1)
try:
    script, target, specns = argv # specns stands for 'Specified Nameserver'
except ValueError:
    print "[*] Error: Please specify a target and nameserver"
    exit(2)

# Define info
info = '''
[*] Author: Colly
[*] Version: Experimental - 1.0
'''

# Define the banner
banner = '''
[*]    _____       _         _                       _         ______ _           _
[*]   / ____|     | |       | |                     (_)       |  ____(_)         | |
[*]  | (___  _   _| |__   __| | ___  _ __ ___   __ _ _ _ __   | |__   _ _ __   __| | ___ _ __
[*]   \___ \| | | | '_ \ / _` |/ _ \| '_ ` _ \ / _` | | '_ \  |  __| | | '_ \ / _` |/ _ \ '__|
[*]   ____) | |_| | |_) | (_| | (_) | | | | | | (_| | | | | | | |    | | | | | (_| |  __/ |
[*]  |_____/ \__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_| |_|    |_|_| |_|\__,_|\___|_|
'''

# Make a list directly from the text file using .split()
listedsubdomains = open('subs.txt').read().split()

def intro():
    print banner,info

def validate(vtarget, vspecns):
    try:
        vtargtrue = False # Create a base value to avoid errors
        socket.gethostbyname(vtarget) # Attempt to resolve the target
        vtargtrue = True # Say that target is valid
        socket.gethostbyname(vspecns) # Attempt to resolve the nameserver
    except socket.gaierror:
        if vtargtrue == True: # Check if earlier step is true
            print "Nameserver Invalid."
            exit(5)
        else:
            print "Target Invalid."
            exit(6)

def scan(target): # Make it take ns as an arg later
    myResolver = dns.resolver.Resolver() # Create a resolver
    for chosensub in listedsubdomains:
        try:
            results = myResolver.query(chosensub+target, "A")
            print chosensub + "." + target
        except dns.resolver.NXDOMAIN:
            False # Boolean filler
        except dns.resolver.NoAnswer:
            False # Should be safe to silently ignore
        except dns.resolver.NoNameservers:
            False # Also is safe to silently ignore


if __name__ == "__main__":
    try: # Put in an error handling loop to prevent Tracebacks
        intro()
        validate(target, specns)
        scan(target)
    except KeyboardInterrupt:
        print "\nOperation interrupted by user."
        exit(3)
    exit(0)