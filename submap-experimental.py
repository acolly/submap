import socket,argparse,os,sys
try: # dnspython error handling
    import dns.resolver
except ImportError: # This is the error given if dnspython isn't intalled
    print("[*] Please install dnspython3 first. Refer to the readme for more information.")
    exit(1)

class submap(object):
    def __init__(self):
        self.banner = '''
[*]    _____       _         _                       _         ______ _           _
[*]   / ____|     | |       | |                     (_)       |  ____(_)         | |
[*]  | (___  _   _| |__   __| | ___  _ __ ___   __ _ _ _ __   | |__   _ _ __   __| | ___ _ __
[*]   \___ \| | | | '_ \ / _` |/ _ \| '_ ` _ \ / _` | | '_ \  |  __| | | '_ \ / _` |/ _ \ '__|
[*]   ____) | |_| | |_) | (_| | (_) | | | | | | (_| | | | | | | |    | | | | | (_| |  __/ |
[*]  |_____/ \__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_| |_|    |_|_| |_|\__,_|\___|_|
'''
        self.info = '''
[*] Author: Colly
[*] Version: Experimental - 3.0
'''
        self.targethelp = "The target domain. Do NOT include 'www'."
        self.nshelp = "The nameserver (optional). If none are provided the system default is used."
        self.loghelp = "The name of the logfile (optional) which will be saved in this directory. Stored as a '.log'." \
                       " Please note that if a logfile exists with the same name it will be truncated without warning."
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("target", help=self.targethelp)
        self.parser.add_argument("-n", dest="nameserver", help=self.nshelp, type=str) # call as args.nameserver
        self.parser.add_argument("-l", dest="logname", action='store', help=self.loghelp, type=str)
        if len(sys.argv)==1:
            self.parser.print_help()
            sys.exit(1)
        self.args = self.parser.parse_args()

    def intro(self):
        print(self.banner)
        print(self.info)

    def logging_intro(self):
        self.logcont = open(self.args.logname+".log", "w")
        self.logcont.write(self.banner+self.info)

    def validate(self,vtarget, vspecns): # Put a 'v' to clarify variables
        vtargtrue = False # Create a base value to avoid errors
        try:
            socket.gethostbyname(vtarget) # Attempt to resolve the target
            vtargtrue = True # Say that target is valid
            if self.args.nameserver != None:
                socket.gethostbyname(vspecns) # Attempt to resolve the nameserver
        except socket.gaierror:
            if vtargtrue == True: # Check if earlier step is true
                pass
                exit(5)
            else:
                pass
                exit(6)
        if self.args.logname != None: # Check if the logging was chosen to avoid wasting time
            while ".log" in self.args.logname:
                print("Error. Please don't include the '.log'. Retype the logname.")
                self.args.logname = input("> ")
                if ".log" not in self.args.logname:
                    break
            if os.path.exists(self.args.logname+".log") == False: # Create the file if it doesn't exist (it shouldn't)
                self.tempcontainer = open(self.args.logname + ".log", "w+")
                self.tempcontainer.close()

    def scan(self,target, ns):
        resolver = dns.resolver.Resolver() # Create a resolver
        if self.args.nameserver != None:
            resolver.nameservers = [socket.gethostbyname(ns)] # Resolve the nameserver and use it
        for chosensub in open('subs.txt').read().split():
            while True:
                try:
                    resolver.query(chosensub+target, "A") # Verify if the chosen subdomain exists
                    print("[*] " + chosensub + '.' + target)
                    if self.args.logname != None:
                        self.logcont.write("[*] " + chosensub + '.' + target + "\n")
                except dns.resolver.NXDOMAIN: # Don't exist
                    break
                except dns.resolver.NoAnswer: # Random stuff
                    break
                except dns.resolver.NoNameservers: # Self explanatory
                    continue
                except AttributeError:
                    pass # Exit if the log doesn't exist
                break

if __name__ == "__main__":
    try: # Put in an error handling loop to prevent Tracebacks
        submapcontainer = submap()
        submapcontainer.intro()
        submapcontainer.validate(submapcontainer.args.target, submapcontainer.args.nameserver)
        if submapcontainer.args.logname != None:
            submapcontainer.logging_intro()
        submapcontainer.scan(submapcontainer.args.target, submapcontainer.args.nameserver)
    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
        if submapcontainer.args.logname != None:
            submapcontainer.logcont.write("[*] Operation interrupted by user.")
        exit(3)
    exit(0)