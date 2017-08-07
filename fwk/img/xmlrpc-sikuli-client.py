# This is client for XML-RPC interface exposed from Sikuli script file
# If you wish, you can do this in any other language with xml-rpc support
# Link to Wikipedia: https://en.wikipedia.org/wiki/XML-RPC
# Note it's Python 3.4

#!/usr/bin/env python3
import xmlrpclib
# import xmlrpc.client # xmlrpclib in Python 2.x
s = xmlrpclib.ServerProxy('http://127.0.0.1:8000')
# s = xmlrpc.client.ServerProxy("http://localhost:8000/") # connecting from the same machine
print(s.click())