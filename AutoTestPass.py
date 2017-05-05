# coding: utf-8

from fwk.utils.utilNetwork.UtilNetwork import UtilNetwork
from ui.flask.uiPortal import app
import sys
reload(sys)

sys.setdefaultencoding('utf8')
if __name__ == '__main__':
    # app.run(debug=True)
    utilNetwork = UtilNetwork()
    app.run(host=utilNetwork.get_local_ip(), port=8080)
