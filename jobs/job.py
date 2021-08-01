import berserk

#API_TOKEN = "{8H7HuEmM6fSQCjG7}"
API_TOKEN = "8H7HuEmM6fSQCjG7"

session = berserk.TokenSession(API_TOKEN)
client = berserk.Client(session=session)

def get_account():
    response = client.account.get()
    return response['id']

def challenge(username, rated, clock_limit=None, clock_increment=None,
               days=None, color=None, variant=None, position=None):
    
    response = client.challenges.create(username,rated)
    
    url = response['challenge']['url']
    return url



print(challenge('ryfern21',False))

