f=open('ctf.txt','r')
points_list=[]

for lines in f:
   points_list.append(lines[-6:-1])
    
print(points_list)

   

   

