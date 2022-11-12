from requests import get
from json import loads
response = get(f'https://ipapi.co/65.110.255.129/json').text
responseinfo = loads(response)
print(responseinfo['region']=="Iowa")