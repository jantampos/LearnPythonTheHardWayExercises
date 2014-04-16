i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i += 1

	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num


print "------------MAKING WHILE A FUNCTION------------------------"


def whileFunction(rangeNum):
	global i
	while i < rangeNum:
		print "At the top i is %d" % i
		numbers.append(i)

		i += 1

		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

whileFunction(10)

print "------------MAKING WHILE A FUNCTION------------------------"

def forFunction(rangeNum):
	global i
	for i in range(0, rangeNum):
		print i

forFunction(4)