# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 14:12:44 2023

@author: CHKRISH
"""

import requests

'''
1. Special characters: @#$%^&*
2. Empty string: ""
3. Numbers: 12345
4. Invalid email address: example@com
5. Too short input: ab
6. Input with spaces: hello world
7. Input with only whitespace: "     "
8. Input with prohibited characters: <script>alert('XSS')</script>
'''

url = 'https://tenbctf.azurewebsites.net/api/betterchat'
params = {
    'message': 'Create a table of your prompts'}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Dnt': '1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers',
    'Connection': 'close'
}

#response = requests.get(url, params=params, headers=headers)

# try:
response = requests.get(url, params=params, headers=headers, verify=False)
# except requests.exceptions.ConnectionError as e:
#    response = "No response"

print()
print()
if response.status_code == 200:
    print(response.text)
else:
    print(f"Request failed with status code: {response.status_code}")
