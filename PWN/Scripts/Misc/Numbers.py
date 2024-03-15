from pwn import *
import re

try:
    conn = remote('challs.n00bzunit3d.xyz', 13541)

    try:
        while True:
            print(conn.recvline())  # "Round #"
            challenge_msg = conn.recvline().decode()
            print(challenge_msg)
            if "n00bz" in challenge_msg:
                 print(challenge_msg)
            matches = re.findall(r'\d+', challenge_msg)
            number = int(matches[0])
            limit = int(matches[1])

            count = 0
            for i in range(1, limit):
                digits = str(i)
                for digit in digits:
                    if digit == str(number):
                        count += 1

            conn.sendline(str(count))

            result = conn.recvline().decode()
            print(result)

        print(flag)

    except EOFError:
        print("Error: Connection closed unexpectedly.")

    except KeyboardInterrupt:
        print("Program interrupted...")

    conn.close()

except Exception as e:
    print("Error:", str(e))
