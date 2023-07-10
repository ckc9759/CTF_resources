import subprocess

def ev(php):
    php=php.replace("abs''","abs(0)")
    out = subprocess.getoutput(f'php -r "echo {php};"')
    if "Parse error" in out:
        print("=======",php,"=======")
        return php,False
    return out,True

fuck = open('chall.php').read()
stack=[]
s=''

def orig(i):
    global fuck
    string=False
    s='('
    while i<len(fuck):
        if fuck[i]=="'" and string:
            string=False
            s+=fuck[i]
        elif fuck[i]=="'":
            string=True
            s+=fuck[i]
        elif fuck[i]=='(' and not string:
            k,j=orig(i+1)
            s+=k
            print(s)
            i=j
        elif fuck[i]==')' and not string:
            s+=')'
            s,check=ev(s)
            if check and s not in ['strstr','abs','array']:
                s=f"'{s}'"
            return s,i
        else:
            s+=fuck[i]
        i+=1
    return s,i

print(orig(0))
