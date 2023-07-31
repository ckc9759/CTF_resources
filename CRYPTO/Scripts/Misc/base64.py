import base64
cipher="fWQobGVxRkxUZmZ8NjQsaHUhe3NAQUch"
ct=base64.b64decode(cipher)
print(ct)
print()

ct2="}d(leqFLTff|64,hu!{s@AG!"
list2=[ct2[i:i+3] for i in range(0,len(ct2),3)]
list3=[i[:2] for i in list2]
print(list2)
print(list3)
