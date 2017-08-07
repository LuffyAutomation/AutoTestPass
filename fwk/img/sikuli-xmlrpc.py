# This is Sikuli script
# More about SimpleXMLRPCServer: https://docs.python.org/2/library/simplexmlrpcserver.html
# import xmlrpclib # is this necessary?

from SimpleXMLRPCServer import SimpleXMLRPCServer


# D:\d\runsikulix.cmd -r C:\Users\L\Desktop\1.sikuli --args 123
def click_it():
    try:
        return "[" + sys.argv[0] + "][" + sys.argv[1] + "]"
        # doubleClick("1494461551532.png")
        return "Success!"
    except Exception as e:
        return e

# s=find('') .h .w .x .y    Screen().h
server = SimpleXMLRPCServer(("127.0.0.1", 8000))
print "Listening on port 8000..."
server.register_function(click_it, "click")
server.serve_forever()