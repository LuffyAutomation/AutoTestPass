# coding: utf-8

from fwk.utils.utilNetwork.UtilNetwork import UtilNetwork
from ui.flask.uiPortal import app
import sys
import webbrowser
reload(sys)

sys.setdefaultencoding('utf8')

def startServer(*args):
    # app.run(debug=True)
    app.run(host=args[0], port=args[1])

def openUrl(*args):
    webbrowser.open("http://" +args[0] + ":" + args[1])

if __name__ == '__main__':
    _UtilNetwork = UtilNetwork()
    local_ip = _UtilNetwork.get_local_ip()
    local_port = "8080"
    webbrowser.open("http://" + local_ip + ":" + local_port)
    app.run(host=local_ip, port=local_port)
