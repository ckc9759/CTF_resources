from binascii import unhexlify
from hashlib import blake2b
from Crypto.Cipher import AES


def main():
    # The embedded hex ciphertext from the binary
    hex_ciphertext = "713d7f2c0f502f485a8af0c284bd3f1e7b03d27204a616a8340beaae23f130edf65401c1f99fe99f63486a385ccea217"
    ciphertext = unhexlify(hex_ciphertext)

    print(f"[*] Brute forcing special character...")

    # Try all printable ASCII characters
    for i in range(32, 127):
        char = chr(i)

        # Hash the character with BLAKE2b (64 bytes)
        hash_result = blake2b(char.encode("utf-8"), digest_size=64).digest()

        # Split: first 32 bytes = key, next 16 bytes = IV
        key = hash_result[:32]
        iv = hash_result[32:48]

        # Decrypt with AES-CBC
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext)

        # Remove PKCS7 padding
        pad_len = plaintext[-1]
        if 1 <= pad_len <= 16:
            plaintext = plaintext[:-pad_len]

        # Check if it looks like a flag
        decoded = plaintext.decode("utf-8", errors="ignore")
        if "scriptCTF{" in decoded:
            print(f"[+] Found special character: '{char}' (ASCII {i})")
            print(f"[+] Flag: {decoded}")

            # Generate example password
            password_length = 10
            special_pos = int(0.6 * password_length)  # Position 6 for length 10
            password = ["A"] * password_length
            password[special_pos] = char
            example_password = "".join(password)

            print(f"[+] Example working password: {example_password}")
            return

    print("[-] No flag found!")

main()
