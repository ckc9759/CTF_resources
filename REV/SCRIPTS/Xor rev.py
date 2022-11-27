enc_line="kjfbewnlfnlkwemmwadmlfwk"
#read all possible keys from random.txt
file1=open('random.txt','r')
lines1=file1.readlines()
for line in lines1:
  key=line.strip()
  print(key)
