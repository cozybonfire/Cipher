# File:        cipher.py
# Programmer:  Gabriel Ruiz (github.com/cozybonfire)
# Description: Main file for Cipher program, containing UI.

# TO ADD A NEW COMMAND:
# - IMPORT IT FROM CIPHERUTILS
# - ADD IT TO THE "COMMANDS" LIST
# - CREATE ITS USAGE DEF
# - ADD IT TO THE MANUAL
# - ADD AN ELIF FOR THAT COMMAND
# - ACCOUNT FOR POSSIBLE USAGE ERRORS WITHIN THAT ELIF

# TODO LIST:
# - TEST FOR PYTHON 3 AND CATCH EXCEPTION; PRINT MESSAGE
# - ALLOW FOR MATH EXPRESSIONS AS ARGUMENTS TO COMMANDS

import fractions, manual, simpleeval
from cipher_utils import alphaexp, binexp, divmod, is_prime, pad, quadres
from manual import man

print("Welcome to Cipher! Type \"help\" to see a list of commands.\n")
while True:
    cmd_str = input("> ")
    cmd = cmd_str.split()
    if len(cmd) == 0:
        continue
    print()

    if cmd[0] == "q" or cmd[0] == "quit":
        if len(cmd) > 1:
            print("Odd usage, but I'm going to assume you want to quit.")
        break

    elif cmd[0] == "alphaexp":
        if len(cmd) != 2 or not cmd[1].isdigit():
            print(manual.USAGE_ALPHAEXP)
            continue
        alphaexp(int(cmd[1]))

    elif cmd[0] == "binexp":
        if len(cmd) != 2 or not cmd[1].isdigit():
            print(manual.USAGE_BINEXP)
            continue
        binexp(int(cmd[1]))

    elif cmd[0] == "divmod":
        if len(cmd) != 3 or not (cmd[1].isdigit() and cmd[2].isdigit()):
            print(manual.USAGE_DIVMOD)
            continue
        divmod(True, int(cmd[1]), int(cmd[2]))

    elif cmd[0] == "gcd":
        if len(cmd) != 3 or not (cmd[1].isdigit() and cmd[2].isdigit()):
            print(manual.USAGE_GCD)
            continue
        print(fractions.gcd(int(cmd[1]), int(cmd[2])))

    elif cmd[0] == "help":
        if len(cmd) > 2:
            print(manual.USAGE_HELP)
            continue
        if len(cmd) == 1:
            print("Available commands:")
            for command in manual.commands:
                print("\t" + command)
            print("Type \"help [command]\" to learn more.")
            print("\nCipher can also interpret basic mathematical "
                  + "expressions at the command line.")
            print("Type \"help math\" to learn more.")
        else:
            print(man.get(cmd[1], manual.CMD_NOT_RECOGNIZED))

    elif cmd[0] == "is_prime":
        if len(cmd) != 2 or not cmd[1].isdigit():
            print(manual.USAGE_IS_PRIME)
            continue
        print(is_prime(int(cmd[1])))

    elif cmd[0] == "info":
        if len(cmd) > 1:
            print("Odd usage, but I'm going to assume you want info:")
        print(man.get("program_info"))

    elif cmd[0] == "license":
        if len(cmd) > 1:
            print("Odd usage, but I assume you want the license:\n");
        print(man.get(cmd[0]))

    elif cmd[0] == "quadres":
        if len(cmd) != 2 or not cmd[1].isdigit():
            print(manual.USAGE_QUADRES)
            continue
        quadres(int(cmd[1]))

    else:
        try:
            print(simpleeval.simple_eval(cmd_str))
        except (simpleeval.InvalidExpression, KeyError, SyntaxError):
            print(manual.CMD_NOT_RECOGNIZED)
    print()
