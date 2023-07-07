#f=open('ctf.txt','r')
#points_list=[]

#for lines in f:
   #points_list.append(lines[-6:-1])
    
#print(points_list)

#---Update

'''f=open('ctf.txt','r')

points_list=[]

for lines in f:
   if lines[-7].isnumeric():
      points_list.append(lines[-7:-1])
   else:
      points_list.append(lines[-6:-1])
   
print(points_list)
points_list=[eval(i) for i in points_list]
points_list.sort(reverse=True)
print()
print(points_list)
'''

#---Update 2

f=open('ctf.txt','r')

points_list=[]

for lines in f:
   if lines[-7].isnumeric():
      points_list.append(lines[-7:-1])
   else:
      points_list.append(lines[-6:-1])
   
print(points_list)
points_list=[eval(i) for i in points_list]
points_list.sort(reverse=True)
print()
print(points_list)
print()

sum=0.0
for i in range(9):
   sum+=points_list[i]
   
sum+=2*23.91
print(f'sum={sum}')


   


   

   

