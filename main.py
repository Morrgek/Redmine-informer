#coding: utf-8
from hypchat import HypChat
import requests
import json
from pprint import pprint
from inspect import getmembers
from redmine import Redmine
import tornado.ioloop
import tornado.web
import tornado.httpserver


class IssueUpdateHandler(tornado.web.RequestHandler):
    def post(self):
        self.write('Hello')
        print('test1')
        data=json.loads(self.request.body)
        message=data["item"]['message']['message']
        index1=message.find("issues")+7
        index2=message.rfind("/")
        if index2<index1: index2=len(message)
        s =int(message[index1:index2])
        redmine = Redmine('http://redmine.vigroup.ru', key='eded47b9c0e8856b08fb184beb8a3c34c3aa0ab4')
        issue = redmine.issues.get(s)

        mes = 'Link: <a href="http://redmine.vigroup.ru/issues/' + str(issue.id) + '">http://redmine.vigroup.ru/issues/' + str(issue.id) + "</a><br>""Name: " + issue.subject + '<br>Responsible: ' + issue.assigned_to.name
        pprint ((data))

        url = "https://api.hipchat.com/v2/room/2106789/notification?auth_token=8tea2EhoyH7hYKSQSdzGTD8YKgAiUByU8PmabZxV"
        header = {"Content-Type": "application/json","Encoding":"utf8", "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)"}
        content = {"color": "green", "message":  mes, "notify": 'true', "message_format": "html"}
        postHipChat = requests.request('POST', url, headers=header, timeout=30, data=json.dumps(content))


def get(self):
    self.write('GET')


app = tornado.web.Application([
    (r"/", IssueUpdateHandler),
])
if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(app)
    server.bind(3737, '127.0.0.1')
    server.start(1)
    tornado.ioloop.IOLoop.current().start()

