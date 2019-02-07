from fbchat import Client, log
from fbchat.models import *

import apiai, codecs, json
import email_password

class PooBot(Client):

    def apiaiCon(self):
        self.CLIENT_ACCESS_TOKEN = "735d6b70efd24e25b866eacc7eb6d95a"
        self.ai = apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
        self.request = self.ai.text_request() #Questions are stored on request
        self.request.lang = 'de' #de = Default i.e. English
        self.request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    def onMessage(self,author_id = None,message_object=None,thread_id=None,thread_type=ThreadType.USER,**kwargs):
        self.markAsRead(author_id)

        log.info("Message {} from {} in {}".format(message_object,thread_id,thread_type))

        #Establishing a Connection now
        self.apiaiCon()

        #Message Text
        msgText = message_object.text

        self.request.query = msgText

        response = self.request.getresponse()

        #obj is the list of response
        obj = json.load(response)
        #
        # with open('data.txt', 'w') as outfile:
        #     json.dump(obj, outfile)

        reply = obj['result']['fulfillment']['speech']

        # try:
        #     reply = obj['result']['fulfillment']['speech']
        # except:
        #     reply = "My Creator Sir Prajwol is currently not here. He is busy with his work. "
        #     pass

        if author_id != self.uid:
            self.send(Message(text = reply), thread_id=thread_id, thread_type=thread_type)

        self.markAsDelivered(author_id,thread_id)

client = PooBot(email_password.email,email_password.password)
client.listen()
