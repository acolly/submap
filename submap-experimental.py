import socket,argparse

# Error handling for dnspython
try:
    import dns.resolver
except ImportError: # This is the error given if dnspython isn't intalled
    print "[*] Please install dnspython first. Refer to the readme for more information."
    exit(1)

targethelp = "The target domain. Do NOT include 'www'."
nshelp = "The nameserver (optional). If none are provided the system default is used."

# Create argparse supplements
parser = argparse.ArgumentParser()
parser.add_argument("target", help=targethelp)
parser.add_argument("-n", dest="nameserver", help=nshelp, type=str) # dest for aesthetics and nshelp for compactness
args = parser.parse_args()
# Define info
info = '''
[*] Author: Colly
[*] Version: Experimental - 2.0
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

def intro(): # Simple wrapper to save space
    print banner,info

def validate(vtarget, vspecns): # Put a 'v' to clarify variables
    try:
        vtargtrue = False # Create a base value to avoid errors
        socket.gethostbyname(vtarget) # Attempt to resolve the target
        vtargtrue = True # Say that target is valid
        if args.nameserver != None:
            socket.gethostbyname(vspecns) # Attempt to resolve the nameserver
    except socket.gaierror:
        if vtargtrue == True: # Check if earlier step is true
            print "Nameserver Invalid."
            exit(5)
        else:
            print "Target Invalid."
            exit(6)

def scan(target, ns):
    myResolver = dns.resolver.Resolver() # Create a resolver
    if args.nameserver != None:
        myResolver.nameservers = [socket.gethostbyname(ns)] # Resolve the nameserver and use it
    for chosensub in listedsubdomains:
        try:
            myResolver.query(chosensub+target, "A") # Verify if the chosen subdomain exists
            print "[*] " + chosensub + '.' + target
        except dns.resolver.NXDOMAIN:
            False # Boolean filler
        except dns.resolver.NoAnswer:
            False # Should be safe to silently ignore
        except dns.resolver.NoNameservers:
            False # Also is safe to silently ignore


if __name__ == "__main__":
    try: # Put in an error handling loop to prevent Tracebacks
        intro()
        validate(args.target, args.nameserver)
        scan(args.target, args.nameserver)
    except KeyboardInterrupt:
        print "\nOperation interrupted by user."
        exit(3)
    exit(0)