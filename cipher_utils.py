# File:        cipher_utils.py
# Programmer:  Gabriel Ruiz (github.com/cozybonfire)
# Description: File containing all of Cipher's utility functions.

def alphaexp(n):
    n_str = str(n)
    vec = []
    alpha = ""
    exponent = 0

    while n - 26 ** exponent > 0:
        exponent = exponent + 1
    exponent = exponent - 1

    while exponent >= 0:
        if(n - 26 ** exponent >= 0):
            vec.append([(int)(n / 26 ** exponent), exponent])
            alpha += chr((int)(n / 26 ** exponent) + 65)
            n = n % 26 ** exponent
        else:
            vec.append([0, exponent])
            alpha += "A"
        exponent = exponent - 1

    print(n_str + " translates to " + alpha + ":\n")
    for p in vec:
        if p == vec[-1]:
            print("[" + str(p[0]) + " * 26^" + str(p[1]) + "]")
        else:
            print("[" + str(p[0]) + " * 26^" + str(p[1]) + "]", end=" + ")

def binexp(n):
    n_str = str(n)
    vec = []
    exponent = 0

    while n - 2 ** exponent > 0:
        exponent = exponent + 1

    while exponent >= 0:
        if(n - 2 ** exponent >= 0):
            vec.append([2 ** exponent, exponent])
            n = n - 2 ** exponent
        exponent = exponent - 1

    print(n_str + " expanded into powers of 2:\n")
    for p in vec:
        if p == vec[-1]:
            print(str(p[0]) + " [2^" + str(p[1]) + "]")
        else:
            print(str(p[0]) + " [2^" + str(p[1]) + "]", end=" + ")

def divmod(n, d):
    div = (int)(n / d)
    mod = n % d
    print("Quotient: " + str(div) + "\tRemainder: " + str(mod))

def pad(s):
    return "\n" + str(s) + "\n"

def quadres(n):
    s = set()
    vec = []
    print("Quadratic resides mod " + str(n) + ":")
    print("[Note that this function may exclude 0, which can be "
          "considered a quadratic\n residue by default.]\n") 
    for i in range(1, n):
        s.add(i ** 2 % n)
        vec.append([i, i ** 2 % n])
    s = sorted(s)

    print(str((int)((n - 1) / 2)) + " quadratic residues total:")	
    for res in s:
        print(str(res), end=" ")

    print("\n\nList of x^2 mod " + str(n) + ":")
    curr_str = ""
    char_count = 0
    for p in vec:
        curr_str = "[" + str(p[0]) + ":" + str(p[1]) + "]"
        char_count += len(curr_str) + 1
        if char_count > 80:		# TODO: account for user's terminal size
            print("\n\n" + curr_str, end=" ")
            char_count = len(curr_str) + 1 
        else:
            print(curr_str, end=" ")
    print()