import base64
from Crypto.Cipher import AES

ct=base64.b64decode('')
key=base64.b64decode('')

aes=AES.new(key,AES.MODE_ECB)
pt=aes.decrypt(ct)

