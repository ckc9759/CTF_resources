# this DOESN'T work because the key changes each time..

def ecb_byte_at_a_time(known_pt=""):
    known_pt = ("A" * 16) + known_pt

    def enc(pt):
        p.sendline(b"Y")
        p.sendlineafter(b"message:", pt)
        p.readuntil(b"Your message is: ")
        ct = bytes.fromhex(p.readline().decode())
        return ct

    for i in range(MAX_FLAG_LEN):
        padding = 15 - (i % 16)
        pt = "A" * padding
        ct = enc(pt)

        dict_cts = {}
        for c in ALPHABET:
            dict_known_pt = known_pt[len(known_pt)-16+1:len(known_pt)]
            dict_pt = dict_known_pt + c
            dict_cts[c] = enc(dict_pt)

        block_to_attack = (padding + i) // 16
        ct_block_to_attack = ct[block_to_attack * 16: (block_to_attack + 1) * 16]

        for c in ALPHABET:
            match = True
            for j in range(16):
                if ct_block_to_attack[j] != dict_cts[c][j]:
                    match = False
                    break

            if match:
                known_pt += c
                print(f"{known_pt[16:]}")
                break

        if "}" in known_pt:
            return known_pt[16:]
