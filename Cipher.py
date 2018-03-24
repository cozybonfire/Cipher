# main file for Cipher program

# PROCESS FOR ADDING A NEW COMMAND:
# - IMPORT IT FROM CIPHERUTILS
# - ADD IT TO THE "COMMANDS" LIST
# - CREATE ITS USAGE DEF
# - ADD IT TO THE MANUAL
# - ADD AN ELIF FOR THAT COMMAND
# - ACCOUNT FOR POSSIBLE USAGE ERRORS WITHIN THAT ELIF

# TODO LIST:
# - TEST FOR PYTHON 3 AND CATCH EXCEPTION; PRINT MESSAGE
# - ALLOW FOR MATH EXPRESSIONS AS ARGUMENTS TO COMMANDS

import simpleeval
from CipherUtils import alphaexp, binexp, divmod, pad, quadres

CMD_NOT_RECOGNIZED = "Command or argument not recognized (try \"help\")."
COPYRIGHT = "(c) 2018 Gabriel Ruiz"
USAGE_ALPHAEXP = "Usage: alphaexp (int)n"
USAGE_BINEXP = "Usage: binexp (int)n"
USAGE_DIVMOD = "Usage: divmod (int)n (int)d"
USAGE_HELP = "Usage: help [command]"
USAGE_INFO = "Usage: info"
USAGE_Q = "Usage: q (or quit)"
USAGE_QUADRES = "Usage: quadres (int)n"
USAGE_QUIT = "Usage: quit (or just q)"
VERSION = "v0.0 (alpha)"

commands = ["alphaexp", "binexp", "divmod", "help", "info", "quadres", 
			"quit"]

manual = {
"alphaexp": USAGE_ALPHAEXP
	+ "\nGiven a number encoded in decimal using addition base 26, decode "
	+ "and print the \nmessage as well as its breakdown.",
"binexp": USAGE_BINEXP
	+ "\nProvides the binary expansion of n.",
"divmod": USAGE_DIVMOD
	+ "\nPrints the result of n / d (integer division, i.e. fraction "
	+ "truncated), as well \nas n % d, the remainder.",
"help": USAGE_HELP 
	+ "\nProvides detailed information on using Cipher's commands."
	+ "\nFor program information, use \"info\".",
"info": USAGE_INFO 
	+ "\nProvides general information about Cipher."
	+ "\nFor assistance with using commands, use \"help\".",
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

print("Welcome to Cipher! Type \"help\" to see a list of commands.")
while True:
	cmd_str = input("\n> ")
	cmd = cmd_str.split()
	print()

	if cmd[0] == "q" or cmd[0] == "quit":
		if len(cmd) > 1:
			print("Odd usage, but I'm going to assume you want to quit.")
		break

	elif cmd[0] == "alphaexp":
		if len(cmd) != 2 or not cmd[1].isdigit():
			print(USAGE_ALPHAEXP)
			continue
		alphaexp(int(cmd[1]))

	elif cmd[0] == "binexp":
		if len(cmd) != 2 or not cmd[1].isdigit():
			print(USAGE_BINEXP)
			continue
		binexp(int(cmd[1]))

	elif cmd[0] == "help":
		if len(cmd) > 2:
			print(USAGE_HELP)
			continue
		if len(cmd) == 1:
			print("Available commands:")
			for command in commands:
				print("\t" + command)
			print("Type \"help [command]\" to learn more.")
			print("\nCipher can also interpret basic mathematical "
				  + "expressions at the command line.")
			print("Type \"help math\" to learn more.")
		else:
			print(manual.get(cmd[1], CMD_NOT_RECOGNIZED))

	elif cmd[0] == "divmod":
		if len(cmd) != 3 or not (cmd[1].isdigit() and cmd[2].isdigit()):
			print(USAGE_DIVMOD)
			continue
		divmod(True, int(cmd[1]), int(cmd[2]))

	elif cmd[0] == "info":
		if len(cmd) > 1:
			print("Odd usage, but I'm going to assume you want info:")
		print(manual.get("program_info"))

	elif cmd[0] == "license":
		if len(cmd) > 1:
			print("Odd usage, but I assume you want the license:\n");
		print(manual.get(cmd[0]))

	elif cmd[0] == "quadres":
		if len(cmd) != 2 or not cmd[1].isdigit():
			print(USAGE_QUADRES)
			continue
		quadres(int(cmd[1]))

	else:
		try:
			print(simpleeval.simple_eval(cmd_str))
		except (simpleeval.InvalidExpression, KeyError, SyntaxError):
			print(CMD_NOT_RECOGNIZED)
