# from tgtg import TgtgClient

# client = TgtgClient(email=data['email'])
# credentials = client.get_credentials()
# print(credentials)


from tgtg import TgtgClient
import json
from pprint import pprint

f = open('tgtg-tokens.json')

data = json.load(f)

client = TgtgClient(access_token=data['accessToken'], 
                    refresh_token=data['refreshToken'], 
                    user_id=data['userID'])

# You can then get some items, by default it will *only* get your favorites
# items = client.get_items()
# print(items)

# To get items (not only your favorites) you need to provide location informations
items = client.get_items(
    favorites_only=True,
    latitude=40.74793817710335,
    longitude=-73.9423128698922,
    radius=10,
)


print(items[0]['display_name'])
print(items[0]['items_available'])