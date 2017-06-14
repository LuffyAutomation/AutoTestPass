import socket


class UtilNetwork:
    def __init__(self):
        pass

    @staticmethod
    def get_local_ip():
        try:
            return socket.gethostbyname(socket.gethostname())  # not work in Mac
        except:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
