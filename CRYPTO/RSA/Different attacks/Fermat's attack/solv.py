from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

g = 3
P = 121407847840823587654648673057258513248172487324370407391241175652533523276605532412599555241774504967764519702094283197762278545483713873101436663001473945726106157159264352878998534133035299601861808839807763182625559052896295039354029361792893109774218584502647139466059910154701304129191164513825925289381
ciphertext = b'S\x00\xe7%\xcd\xec\xad\x9a\xe1lO\x80\xd6\r\xa5\x00\x19Y\x18\x7f\xa1\x9cx\x98\xb08n~-\rj2\xd4d\xd2\xda\xa6\xd0\r#7\xee-\\\xb4\x10\x98\x8f'
Hint = 1

a = P-1

for i in range(1,100):
    key = long_to_bytes(a*i)[:16]
    plaintext = AES.new(key, AES.MODE_ECB).decrypt(ciphertext)
    if b'byuctf' in plaintext:
        print(unpad(plaintext, AES.block_size))
        quit()
