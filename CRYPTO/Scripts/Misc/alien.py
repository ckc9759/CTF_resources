D = {}
for hint in "T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24".split(' '):
    D[int(hint[1:])] = hint[:1]
print(''.join(D[k] for k in sorted(D.keys())))

#-- Alternate

 import time
    enc = 'T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24'

    splitted = enc.split(' ')

    for c in splitted:
        char = c[0]
        place = int(c[1:])
        time.sleep(0.1)
        print('\033[C' * (place) + char, end='')
        print('\r', end='')
    print()
