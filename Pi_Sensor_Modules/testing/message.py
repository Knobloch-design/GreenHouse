# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACbf396ebc5e1bbc372058a638333639a0"
auth_token = "d033deee8f868450922759c6b0bc5a7c"
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello from Twilio",
  from_="+18449043320",
  to="+13198550756"
)

print(message.sid)
