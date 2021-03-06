# File:        manual.py
# Programmer:  Gabriel Ruiz (github.com/cozybonfire)
# Description: File containing raw data and dictionaries for Cipher.

# Usage constants
CMD_NOT_RECOGNIZED = "Command or argument not recognized (try \"help\")."
COPYRIGHT          = "(c) 2018 Gabriel Ruiz"
USAGE_ALPHAENCODE = "Usage: alphaencode [string]"
USAGE_ALPHAEXP     = "Usage: alphaexp [int]"
USAGE_BINEXP       = "Usage: binexp [int]"
USAGE_DIVMOD       = "Usage: divmod [int] [int]"
USAGE_GCD          = "Usage: gcd [int] [int]"
USAGE_HELP         = "Usage: help [command]"
USAGE_INFO         = "Usage: info"
USAGE_IS_PRIME     = "Usage: is_prime [int]"
USAGE_Q            = "Usage: q (or quit)"
USAGE_QUADRES      = "Usage: quadres [int]"
USAGE_QUIT         = "Usage: quit (or just q)"
VERSION            = "v0.0 (alpha)"

# List of commands 
# Update with each new command so it gets printed when the user types "help".
commands = ["alphaencode", "alphaexp", "binexp", "divmod", "gcd", "help", 
            "info", "is_prime", "quadres", "quit"]

# Dictionary of command information
man = {
"alphaencode": USAGE_ALPHAENCODE
    + "\nGiven a string to encode, return the numeric version of that "
    + "string in terms of \nalpha representation. This means that each "
    + "letter in the string has a value \nbetween 0 and 25, and is "
    + "multiplied by a power of 26 according to its position \nin the "
    + "string in order to compile a unique number."
    + "\n\nNote that in mapping each letter to a value from 0 to 25, "
    + "there must be no \ndigits in the string. Including any digits will "
    + "throw an error message.",
"alphaexp": USAGE_ALPHAEXP
    + "\nGiven a number encoded in decimal using addition base 26, decode "
    + "and print the \nmessage as well as its breakdown.",
"binexp": USAGE_BINEXP
    + "\nProvides the binary expansion of n.",
"divmod": USAGE_DIVMOD
    + "\nPrints the result of n / d (integer division, i.e. fraction "
    + "truncated), as well \nas n % d, the remainder.",
"gcd": USAGE_GCD
    + "\nComputes the greatest common divisor between two integers, "
    + "\ni.e. the highest integer that divides both.",
"help": USAGE_HELP 
    + "\nProvides detailed information on using Cipher's commands."
    + "\nFor program information, use \"info\".",
"info": USAGE_INFO 
    + "\nProvides general information about Cipher."
    + "\nFor assistance with using commands, use \"help\".",
"is_prime": USAGE_IS_PRIME
    + "\nReturns True if the integer argument is prime, False otherwise.",
"license": "MIT License\n"
    + "\nPermission is hereby granted, free of charge, to any person "
    + "obtaining a copy of \nthis software and associated documentation "
    + "files (the \"Software\"), to deal in \nthe Software without "
    + "restriction, including without limitation the rights to \nuse, "
    + "copy, modify, merge, publish, distribute, sublicense, and/or sell "
    + "copies \nof the Software, and to permit persons to whom the "
    + "Software is furnished to do \nso, subject to the following "
    + "conditions:\n"
    + "\nThe above copyright notice and this permission notice shall be "
    + "included in all \ncopies or substantial portions of the Software.\n"
    + "\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY "
    + "KIND, EXPRESS OR \nIMPLIED, INCLUDING BUT NOT LIMITED TO THE "
    + "WARRANTIES OF MERCHANTIBILITY, \nFITNESS FOR A PARTICULAR PURPOSE "
    + "AND NONINFRINGEMENT. IN NO EVENT SHALL THE \nAUTHORS OR COPYRIGHT "
    + "HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER \nLIABILITY, "
    + "WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, "
    + "\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER "
    + "DEALINGS IN THE \nSOFTWARE.",
"math": "Cipher can interpret any mathematical expression which can be "
    + "resolved to an \ninteger or floating point (decimal) value. "
    + "Specifically, it can perform \naddition, subtraction, "
    + "multiplication, division, exponents, and roots with "
    + "\ncorrect order of operations.\n"
    + "\nTo evaluate an exponent, type \"n ** exponent\". For example, "
    + "\"2 ** 5\" would \nevaluate to 32.\n"
    + "\nTo evaluate a square root, type \"n ** (1/2)\". This works for "
    + "any root; simply \nreplace 2 with the root you require.\n"
    + "\nEven Boolean expressions can be evaluated! Use \"and\", \"or\", "
    + "and \"not\".\n"
    + "\nNote that expressions must have consistent grouping; that is, "
    + "the number of \nleft parentheses must match the number of right "
    + "parentheses.",
"program_info": "Cipher is a cryptography program; it has many utility "
    + "functions that apply \nmathematical concepts from cryptography, "
    + "including encryption/decryption \nschemes and key exchanges.\n"
    + "\n\t " + VERSION + " - " + COPYRIGHT + " - github.com/cozybonfire"
    + "\n  Openly provided under the MIT License. Type \"license\" for "
    + "full information.",
"q": USAGE_Q + "\nEnds the program!",
"quadres": USAGE_QUADRES + "\nPrints all quadratic residues mod n.",
"quit": USAGE_QUIT + "\nEnds the program!"
}


