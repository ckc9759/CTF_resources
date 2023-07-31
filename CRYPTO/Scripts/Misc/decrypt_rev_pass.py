import string
def encrypt(a1):
    if a1 == 123 or a1 == 125:
        return 90
    else:
        return (ord(a1) + 7) ^ 0xB

def increment(v):
    return v + 1

def set_flag():
    flag = (
        "PziP97vkc5sA6oJM0KwWEnQX2OFaH0nAFTuS42myr31GYbJIfBSdAFWsLpx8N0v4PzO7aIVQaHrVq6AW8c1K5ZyFXzMeRAOiJ2nWXYy2Pj7x96RzkcA3"
        "inNqlDOBLKZ4rNFYGTn0Cl5U9aX2WIH1cOyIbm2AZ0k31u7FrxBECKPpMhYVUyvA5LfgXcW9eDSMTBlsorR22laXN3e8<qSCmwK0Do9bJzYvd5YgG3dR"
        "BhwMvOp2qS08UWQKtLQbphJTXLd2~fktr45ES7OK3x0yNqu1XSC9nA`rGpBvQlbDktjIxLm2KlVYnXw0mpt5aOe8B4grGXFe06gaZv3PYdpS4CDquJnm"
        "kR1Mn6sKScF3vV7pdzYfTkBRbqGbzu2wtPHkXsx1pK14ojTfJYIe0PpU1TjDKaW85uZ2mlFHYMSEkBvKo6WIdTnVRewMPk|3pU1SjNErN7s0HYlp9tMq"
        "AmBh0dXD4VaK8NZWU1fnrsQaEc5Bht09eHwxDSpWj0ahd5rtIzyKETxUq9CkXC8DAP37Kc1UqOvdb2GT0Yvxuh1grzfdR4JiVpo83QOEWlL2<Bt9Xm7Q"
        "5RNkljfOZogB8ctIzyra9wF0RKycTJjvZfDlm6o75QsG`2laXN3e85qSCmwK0Do9bJzYvdZE6"
    )
    return flag

def main():
    v3 = 0
    flag = set_flag()
    input_len = 26

    s= ""
    for x in range(input_len):
        for i in string.printable:
            input_test = s+i
            while encrypt(i) == ord(flag[26 * v3]):
                print("Found index " + str(v3) + " " + s)
                s += i
                v3 = increment(v3)
                if v3 == 25:
                    print("Correct password")
                    print(s)
                    exit(0)
    #print("Wrong password")
    #exit(0)

if __name__ == "__main__":
    main()
