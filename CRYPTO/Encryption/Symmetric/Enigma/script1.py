for r2 in rotors: 
    for r3 in rotors: 
        for r in reflectors: 
            machine = EnigmaMachine.from_key_sheet( 
               rotors=' '.join(['Gamma', r1, r2, r3]), 
               reflector=r, 
               ring_settings='D I C T', 
               plugboard_settings='fv cd hu ik es op yl wq jm'.upper()) 
            machine.set_display('BENE') 
            temp = machine.process_text('zkrtwvvvnrkulxhoywoj') 

            if 'CTF' in temp: 
                print(temp, r1, r2, r3, r) 
