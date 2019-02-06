from fbchat import Client, log
from fbchat.models import *

import email_password

class PooBot(Client):

    def onMessage(self,author_id = None,message_object=None,thread_id=None,thread_type=ThreadType.USER,**kwargs):
        self.markAsRead(author_id)

        log.info("Message {} from {} in {}".format(message_object,thread_id,thread_type))

        msgText = message_object.text

        reply = 'Hello Sir/Madam, Prajwol Sir is not here right now. Please Leave a message. I will get back to him as soon as possible.'
        if author_id != self.uid:
            self.send(Message(text = reply), thread_id=thread_id, thread_type=thread_type)

        self.markAsDelivered(author_id,thread_id)

client = PooBot(email_password.email,email_password.password)
client.listen()
