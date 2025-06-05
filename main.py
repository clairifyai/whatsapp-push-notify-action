import os
from twilio.rest import Client

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Yay! User guide updated. Change log at docs.clairify.ai',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:'+os.environ['to_whatsapp_no']
                          )

print("Message ID:",message.sid)
