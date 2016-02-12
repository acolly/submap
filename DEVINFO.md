Developer Information
=====================

TODO
----
Include dnspython inside the submap project
Multiple targets for efficiency 
Multiple dns requests to speed it up
Make a stripped down "core" version
Ouput errors to an external logfile

Exit Codes
----------
1 : dnspython not installed
2 : not enough values specified
3 : keyboard interrupt
4 : no internet connecton
5 : target specified is invalid
6 : invalid nameserver

Experimental
------------
Errors dns.resolver.NoAnswer & dns.resolver.NoNameservers
can be safely ignored silently. They maybe want to
be logged to an external file to judge reliablity
of the nameserver at a future date. Note the results you 
get are based on what nameserver you use to a large degree.
