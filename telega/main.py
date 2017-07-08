import urllib2,json,sys

class TelegramClass:
 self_token = ""
 self_debug = False
 def __init__(self,token=False,apilink="https://api.telegram.org/",debug=False):
  if not token or not apilink:
   print "You must give me your token!"
   sys.exit(1)
   return False
  global self_token
  global self_debug
  self_debug = debug
  self_token = token
  print "Bot initted. "
  print "Try getme"
  infobot = self.response("getme") 
  print "connection good: " + str(infobot["ok"])  
  print "ID of bot: " + str(infobot["result"]["id"]) + "\n"+"FirstName: "+infobot["result"]["first_name"]+"\nUsername: " + infobot["result"]["username"]

 def response(what,*par):
  paramsful=""
  for a in par:
   paramsful = paramsful+"/"+str(a)
  link = "https://api.telegram.org/"+"bot"+self_token+paramsful
  if self_debug:
   print "open: " + link
  try:
   req = urllib2.Request (link,headers={ 'User-Agent': 'Mozilla/5.0' })
   response = urllib2.urlopen(req)
   return json.loads(response.read())
  except urllib2.HTTPError as err:
   if err.code == 404:
    print "404 error, maybe you give do not worked token"
   else:
    print "Some error\n"+err.read()

 def getUpdates(self):
  updates = self.response("getUpdates")
  if not updates['ok']:
   return False
  return updates["result"]
 
 def getMessages(self):
  messages = []
  updates = self.getUpdates()
  for update in updates:
   if self_debug:
    print update["message"]
   messages.append(update["message"])
  return messages

 def sendMessage(self,to,message):
  self.response("sendMessage?chat_id="+"@"+to+"&text="+message)

 def JoinToChannel(self,channel,Message="Hello bitches"):
  self.sendMessage(channel,Message)
