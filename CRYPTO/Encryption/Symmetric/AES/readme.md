### NOTES 

---

[AES](https://www.ctfnote.com/crypto/aes)

AES-128

```py
From the 128 bit key, 11 separate 128 bit "round keys" are derived: one to be used in each AddRoundKey step.
The bytes of the first round key are XOR'd with the bytes of the state.
This phase is looped 10 times, for 9 main rounds plus one "final round"
