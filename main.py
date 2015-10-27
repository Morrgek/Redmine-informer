__author__ = 'Yuliya'
from hypchat import HypChat
import requests
import json
from pprint import pprint
from inspect import getmembers
from redmine import Redmine
hc = HypChat("I0g2pkHddWb96RxSYLYPUuujIXUtdxQpDiTd8PQX")
redmine = Redmine('http://redmine.vigroup.ru/', username='karpenko', password='wearethebest2015')
issue = redmine.issue.get(8359, include='children,journals,watchers')

print (getmembers(issue))
print ((issue.assigned_to.name))

room=hc.get_room('2093649')
print(dir(room))
print (room.create_webhook)



url = "https://api.hipchat.com/v2/room/2093649/notification?auth_token=HJ8tw3CeevuCTpVKtrkUzkXjvv7Fur3aJuhdJ3PB"
header = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)"}
mes="Ссылка: http://redmine.vigroup.ru/"+str(issue.id)+"\n""Название: "+issue.subject+"\n""Ответсвенный: "+issue.assigned_to.name
content = {"color": "green", "message": mes, "notify": 'false', "message_format": "text"}
postHipChat = requests.request('POST', url, headers=header, timeout=30, data=json.dumps(content))

