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
			return str(segmentOne)+ "-" + segmentTwo


def genOEM():
	SegmentOneP1 = random.randint(0,366)
	SegmentOneP1 = str(SegmentOneP1)

	while len(SegmentOneP1) < 3:           
		SegmentOneP1 = SegmentOneP1.zfill(3)

	print("seg1p1")

	SegmentOneP2 = random.randint(3,95)
	SegmentOneP2 = str(SegmentOneP2)

	while len(SegmentOneP2) < 2:     
		SegmentOneP2 = SegmentOneP2.zfill(2)

	print("seg1p2")
	
	SegmentTwo = "OEM"

	SegmentThree = 0
	complete = False
	while not complete:
		num = random.randint(111111,999999)
		num = str(num)
		num = num.zfill(7)

		final = 0
		for chars in num:
			final+=int(chars)

		if final % 7 == 0:
			SegmentThree = num
			complete = True

	print('seg3')
    	
	SegmentFour = random.randint(0,99999)
	SegmentFour = str(SegmentFour)
	while len(SegmentFour) < 5:
		SegmentFour.zfill(5)

	print('seg4')
	
	return (SegmentOneP1+SegmentOneP2+"-"+SegmentTwo+"-"+SegmentThree+"-"+SegmentFour)


def main():
	import easygui

	import pyperclip
	while True:
		keytype=easygui.buttonbox(title="winkeygen", msg="Welcome to WinKeygen \n \nPlease select your required key type", choices=["Retail", "OEM", "Quit"])
		if keytype == "Retail":
			print("gen: retail")
			key = nonOEM()
			print("generated: retail")
			message = "Generated! \nKey: " + key
			easygui.msgbox(title="winkeygen", msg=message)
			pyperclip.copy(key)


		if keytype == "OEM":
			print("gen: oem")
			key = genOEM()
			print("generated: oem")
			message = "Generated! \nKey: " + key
			easygui.msgbox(title="winkeygen", msg=message)
			pyperclip.copy(key)


		if keytype == "Quit":
			break
		
if __name__ == "__main__":
	main()
