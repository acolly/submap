Submap: Subdomain Mapper
========================

What is it?
-----------

Submap is a small python script that attempts to resolve
a list of sub-domains against a given target using
'subs.txt' as a sub-domain source list. I would love to
see the results of you guys messing around with the code
so just hit me up with an email.

Features
--------

Submap  uses Python 2.7 and submap-stable only uses builtin modules at
the moment unless you use the experimental version which uses Python 3.5 
and dnspython. It takes the subdomains it needs to use from 'subs'.txt 
which contains a very extensive list, feel free to add more to it.

The Latest Version
------------------

The latest version of submap can be found here.

Experimental
------------

There is an experimental version of submap which I use for
testing out new techniques and methods. Currently it supports
custom nameservers, granular dns queries, improved error handling
and target/nameserver validation. Eventually experimental 
features will be incorporated into submap-stable. 

Core
----

Submap core is a tiny and extremely compact version of submap. There
are two versions of it: comment and unread. Comment is a readable
version of the file whereas unread is far harder to read. 

Basic Usage
-----------

To use, simply ```cd``` to the directory with ```submap.py``` 
and ```subs.txt```. Ensure that ```subs.txt``` is there. Then do
```python submap.py [target]``` and replace ```[target]``` 
with the url you wish to scan.

For the experimental version there is a ```nameserver``` flag
you can use: ```python submap-experimental.py [-h] [-n NAMESERVER] target ```.
The nameserver can be in url or IPv4 format though the target has to
be a url.

Documentation
-------------

Documentation is currently under development though it isn't a priority. 
When it is finished it will most likely be located at the url given:
'colly.gitub.io/submap/doc'. There is a rough document called DEVINFO
which can be used in the meantime.

Installation
------------

There is no real installation as the only things you need
is Python 2.7, the script itself and 'subs.txt'. The first
can be downloaded here: 'https://www.python.org/downloads/'
while the rest can be downloaded from here. 
The exception is the experimental version of submap which 
requires dnspython. It can easily be downloaded by doing  
```sudo pip install dnspython``` on OSX and Linux. On Windows 
just ```pip install dnspython``` should work though keep in 
mind submap is not tested at all on Windows.

Licensing
---------

Submap is licensed under the MIT license. See the license
file for more information.

Contacts
--------

If you need to reach me urgently hit me up at 'acolly@protonmail.com'.
Alternatively for bug fixes or requesting features please open an 
issue here.

Reporting Bugs
--------------

Please use the github issue tracker to open issues. When
reporting bugs, please provide as much detail as possible.
This includes the os you are on and its version, a console
log and what version of python you have.