# All of Crypto's utility functions

def alphaexp(n):
	vec = []
	alpha = ""
	flag = False
	exponent = 1000
	for i in range(0, exponent + 1):
		if(n - 26**exponent >= 0):
			flag = True
			vec.append([divmod(False, n, 26**exponent)[1], exponent])
			alpha += chr(divmod(False, n, 26**exponent)[1] + 65)
			n = divmod(False, n, 26**exponent)[0]
		elif(flag):
			vec.append([0, exponent])
			alpha += "A"
		exponent = exponent - 1
	print(alpha)
	print(vec)

def binexp(n):
	vec = []
	exponent = 1000
	for i in range(0, exponent + 1):
		if(n - 2**exponent >= 0):
			vec.append([2**exponent, exponent])
			n = n - 2**exponent
		exponent = exponent - 1
	for p in vec:
		if p == vec[-1]:
			print(str(p[0]) + " [2^" + str(p[1]) + "]", end="")
		else:
			print(str(p[0]) + " [2^" + str(p[1]) + "]", end=" + ")
	print()

def divmod(prnt, n, d):
	count = 0
	while n >= 0:
		n = n - d
		count = count + 1
	n = n + d
	count = count - 1
	if prnt:
		print("quotient: " + str(count) + "\tremainder: " + str(n))
	return [n, count]

def pad(s):
	return "\n" + str(s) + "\n"

def quadres(n):
	s = set() 
	for i in range(1, n + 1):
		s.add(i**2 % n)
		print(str(i) + ":\t" + str(i**2 % n))
	s = sorted(s)

	print()
	print(str((int)((n + 1) / 2)) + " quadratic residues total:")	
	for res in s:
		print(str(res), end=" ")
	print("")
