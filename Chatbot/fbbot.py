from fbchat import Client, log
from fbchat.models import *

import apiai, codecs, json
import email_password

counter = 0
defaultMsg = "Hello. I am Geekuru. Unfortunately, the person that you are trying to reach is not  available at the moment. I will have him mailed your message. Please leave a message."
class chatbot(Client):

    def apiaiCon(self):
        self.CLIENT_ACCESS_TOKEN = "802a31efa082481eb9d9415c5a408e9b"
        self.ai = apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
        self.request = self.ai.text_request() #Questions are stored on request
        self.request.lang = 'de' #de = Default i.e. English
        self.request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    def onMessage(self,author_id = None,message_object=None,thread_id=None,thread_type=ThreadType.USER,**kwargs):

        if thread_type != ThreadType.GROUP:
            self.markAsRead(author_id)

            log.info("Message {} from {} in {}".format(message_object,thread_id,thread_type))

            print("...............................................")
            print(message_object.text)
            print("...............................................")


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

            if author_id != self.uid:
                current_clientID = author_id
                user = client.fetchUserInfo(author_id)[author_id]
                filename = user.name[:4]+author_id
                file = open(filename,"a")
                name1 = user.name+": "
                print(name1)
                file.write(name1)
                file.write(message_object.text)
                file.write("\n\n")
                file.write("Geekuru: ")
                file.write(reply)
                file.write("\n\n")

            if author_id != self.uid:
                global counter
                global defaultMsg
                if thread_type != ThreadType.GROUP:
                    if counter == 0:
                        self.send(Message(text = defaultMsg), thread_id=thread_id, thread_type=thread_type)
                        # self.send(Message(text='', emoji_size=EmojiSize.LARGE), thread_id=thread_id, thread_type=thread_type)
                        counter += 1
                    if counter != 0:
                        self.send(Message(text = reply), thread_id=thread_id, thread_type=thread_type)

            self.markAsDelivered(author_id,thread_id)

client = chatbot(email_password.email,email_password.password)
client.listen()
