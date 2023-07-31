tune = "DC# C#D# C#C C#C DC# C#D# E2 C#5 CA EC# CC DE CA EB EC# D#F EF# D6 D#4 CC EC EC CC# D#E CC E4"
KEYS="A,A#,B,C,C#,D,D#,E,F,F#,1,2,3,4,5,6".split(',')
VALS=[i for i in range(16)]

for c in tune.split(' '):
    out=[]
    for i,x in enumerate(c):
        if (x == '#'):
            out[-1]+=1
        else:
            out.append(VALS[KEYS.index(x)])
    print( chr( int(f"{out[0]:x}{out[1]:x}",16) ), end='')
print()
