from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+1xxxxxxxxx',
    body='I cant believe this works',
    to='+1xxxxxxxxxx'
)

print(message.sid)
