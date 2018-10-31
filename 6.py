# Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both inc)



def perform():
	outlist = [i*i for i in range(1,31) if i>5]
	print(outlist)	


def main():
	#inp = input("Enter numbers") # Ask for input if any
	perform()


if __name__ == '__main__':
	main()