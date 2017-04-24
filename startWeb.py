# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from src.utils.utilNetwork.UtilNetwork import UtilNetwork
from web.flask.webTool import app

if __name__ == '__main__':
    # app.run(debug=True)
    utilNetwork = UtilNetwork()
    app.run(host=utilNetwork.get_local_ip(), port=8080)