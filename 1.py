###Write a Python program to get the largest number from a list. 


def getMax():
	inp = input("Enter numbers")
	lis = inp.split(",")
	
	numbers = [int(x) for x in lis]
	max = numbers[0]
	for item in numbers:
		if item > max:
			max = item
	return max


def main():
	output = getMax()
	print(output)


if __name__ == '__main__':
	main()

'''	
#Key Points	
We have to perform mathematical operations on numbers not strings
list comprehensions : to perform same operation to all elements of list, list comprehensions are useful''
'''