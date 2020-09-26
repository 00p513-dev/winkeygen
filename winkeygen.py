import random

def check(number):
	dissallowedNumbers = [333,444,555,666,777,888,999]
	for num in dissallowedNumbers:
		if number == num:
			return False
	for num in range(0,99):
		if number == num:
			return False
	return True

def nonOEM():
	generated=False
	while not generated:
		valid = False
		while not valid:
			segmentOne = random.randint(111,999)
			#segmentOne = 420
			if check(segmentOne):
				valid = True

		segmentTwo = random.randint(111111,999999)
		segmentTwo = str(segmentTwo)
		segmentTwo += "0"

		final = 0
		for chars in segmentTwo:
			final += int(chars)

		if final % 7 == 0:
			generated=True
			print(str(segmentOne)+ "-" + segmentTwo)

nonOEM()
