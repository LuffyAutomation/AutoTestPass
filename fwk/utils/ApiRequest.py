#coding=utf-8
__author__ = 'Justin'

import os
#import requests
import json

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)


#localhost = "http://localhost:8100"

class request():

    def __init__(self):
        self.method = None
        self.uri = None
        self.path = None
        self.param = None
        self.body = {}
        self.headers={}
        self.response= None
        self.request = None
        self.sessionId = None



    def setRequest(self,method,uri):
        self.uri = uri
        self.method = method
        return self

    def GET(self,uri):
         return self.setRequest("GET",uri)

    def POST(self,uri):
         return self.setRequest("POST",uri)

    def PUT(self,uri):
        return self.setRequest("PUT",uri)

    def DELETE(self,uri):
        return self.setRequest("DELETE",uri)

    def setPath(self,path):
        self.path = path
        return self


    def params(self,key,value):
        if self.param == None:
            self.param+="&"
        self.param+=key.strip()+"="+value.strip()
        return self

    def type(self,type):
        self.headers.setdefault("Content-Type",type)
        return self

    def setbody(self,body):
        self.body=body
        return self


    def execute(self):
        # if not self.path==None:
        #     self.uri+=self.path
        #
        # if self.method=="GET":
        #     self.response = requests.get(self.uri,params=self.param)
        # if self.method=="POST":
        #     self.response =requests.post(self.uri,self.param,self.body,headers=self.headers)
        # print "<<<<<<<<<<<<<<<<<"
        # print self.response.url
        # print self.response.text
        # print self.response.status_code
        #
        # print self.response.headers
        # print self.response.reason
        # requests.session().close()
        # print ">>>>>>>>>>>>>>>>>"
        # return self.response.text
        pass


class wdaRun():
    def __init__(self):
        self.sessionId = None
        self.api = request()
        self.uri = "http://localhost:8100"
        self.getSession()

    def getSession(self):
        json_str=self.api.GET(self.uri).setPath("/status").execute()
        sessionId = json.loads(json_str).get("sessionId")
        self.sessionId = sessionId

    def swipe(self,fromX,fromY,toX,toY,duration=0):
        body = {"fromX": fromX, "fromY": fromY, "toX": toX, "toY": toY, "duration": duration}
        #body = {"fromX": "100", "fromY": "100", "toX": "400", "toY": "100","duration": "0"}
        self.api.POST(self.uri).setPath("/session/" + self.sessionId + "/wda/dragfromtoforduration").setbody(body).type("application/json").execute()

    def home(self):
        self.api.POST(self.uri).setPath("/wda/homescreen").type(
            "application/json").execute()
    def tap(self,x,y):
        body = {"x": x, "y": y}
        self.api.POST(self.uri).setPath("/session/"+self.sessionId+"/wda/tap/null").setbody(body).type(
            "application/json").execute()
    def keys(self,value):
        body = {"value":[value]}
        self.api.POST(self.uri).setPath("/session/"+self.sessionId+"/wda/keys").setbody(
            body).type(
            "application/json").execute()

    # def launchAp(self):
    #
    #     body = {"value": [value]}
    #     self.api.POST(self.uri).setPath("/session/" + self.sessionId + "/wda/keys").setbody(
    #         body).type(
    #         "application/json").execute()

# print "test"
#
# run = wdaRun()
# print "get Session"
# #run.getSession()
# run.swipe(80,100,400,100)
# #run.home()
# run.tap(250,120)
#run.keys("asdfasdfsadfadsf")

# run.home()
# run.keys()
# request.createSessionId(request)
# request.run("swipe")
#request = ApiRequest()

# json_str = request.GET("http://localhost:8100").setPath("/status").execute()
# sessionId = json.loads(json_str).get("sessionId")
# print sessionId
# print request
# body = {"fromX":"100","fromY":"100","toX":"400","toY":"100","duration":"0"}
# #body = "{\"fromX\":\"100\",\"fromY\":\"100\",\"toX\":\"400\",\"toY\":\"100\",\"duration\":\"0\"}"
# print body
# request.POST("http://localhost:8100").setPath("/session/"+sessionId+"/wda/dragfromtoforduration").setbody(body).type("application/json").execute()




