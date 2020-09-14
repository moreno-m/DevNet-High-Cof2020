#!/usr/local/bin/python3

import requests
import json

url = 'https://api.chucknorris.io/jokes/random'
def get_chuck_joke(api):
    getRest = requests.request("GET", api)
    jsonResp = getRest.json()
    return jsonResp

if __name__ == '__main__':
    #  TASK 3 - correct the json statement
    #  This will get the json serial and convert it into string
    joke = json.dumps(get_chuck_joke(url))
    print("\n---TASK4---")
    #   Get the string from above and convert it to a Python dictionary and print the value
    joke = json.loads(joke)['value']
    print(joke)
    #   I could have printed directly by simply doing this:
    #   print(get_chuck_joke(url)['value'])
    #   But, task 3 requested to copmplete the json statement.