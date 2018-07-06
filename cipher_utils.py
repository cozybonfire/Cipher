# File:        cipher_utils.py
# Programmer:  Gabriel Ruiz (github.com/cozybonfire)
# Description: File containing all of Cipher's utility functions.
#              Functions ending with "_util" format the output 
#              appropriately for Cipher's UI, while using a helper to do 
#              the actual work.

import math

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

# Calculates the binary expansion of n. Returns a list of pairs [a, b] 
# such that a = 2^b and the sum of all a's is n.
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
    return vec

def binexp_util(n):
    vec = binexp(n)
    print(n_str + " expanded into powers of 2:\n")
    for p in vec:
        if p == vec[-1]:
            print(str(p[0]) + " [2^" + str(p[1]) + "]")
        else:
            print(str(p[0]) + " [2^" + str(p[1]) + "]", end=" + ")

def divmod(n, d):
    div = (int)(n / d) # TODO n // d?
    mod = n % d
    print("Quotient: " + str(div) + "\tRemainder: " + str(mod))

# Uses Fermat primality testing to verify primality of n without factoring.
# Generates k-many random possible witnesses for n's composite-ness, 
# and then verifies they are all congruent to 1 mod n when raised to (n-1).
def is_prime(n, k):
#    for a in range(1, n):
    return   

def pad(s):
    return "\n" + str(s) + "\n"

# Calculates a^k (mod N) efficiently through repeated squaring.
def power_mod(a, k, N):
    if k == 0: return 1
    exps = [b for [a, b] in binexp(k)]
    result = 1

    for i in range(0, exps[0] + 1):
        if i in exps:
            result = (result * a) % N
        a = (a ** 2) % N

    return result

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

# Returns a list of primes up to and including n.
def sieve_of_eratosthenes(n):
    if n < 2:  return []

    sieve = [i for i in range(2, n + 1)]
    for i in range(0, len(sieve)):
        if sieve[i] != 0:
            for j in range(i + 1, len(sieve)):
                if sieve[j] % sieve[i] == 0:
                    sieve[j] = 0

    return [p for p in sieve if p != 0]
