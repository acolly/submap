import socket,sys
b = '''
Subdomain Finder
By Colly
Author:Colly
Version:Core-1.0
'''
def sc(t):
    for h in open('subs.txt').read().split():
        try:
            socket.gethostbyname(h+'.'+t);print h+'.'+t;print socket.gethostbyname(h+"."+t+"\n")
        except socket.gaierror:
            pass
print b;sc(sys.argv[1])