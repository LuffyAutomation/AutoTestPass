import socket


class UtilNetwork:
    def __init__(self):
        pass

    def get_local_ip(self):
        return socket.gethostbyname(socket.gethostname())
