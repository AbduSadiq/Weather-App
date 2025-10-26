from __future__ import print_function
from random import choice
import time
import weatherapi
from weatherapi.rest import ApiException
from pprint import pprint

configuration = weatherapi.Configuration()
configuration.api_key['key'] = '33c4c4c4a5064a6b9cd74921252610'

choice = input('Hello, press 1 to get started, and 2 to exit.')

if choice == '1':
    api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration))
    q = int(input('Please enter your zipcode.'))

    api_response = api_instance.realtime_weather(q)
    pprint(api_response)

elif choice == '2':
    print('Have a great day.')

else:
    print('Invalid Choice.')
