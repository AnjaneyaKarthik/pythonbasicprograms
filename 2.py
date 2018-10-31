#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings


def perform(lis):
	outputCount = 0
	for item in lis:
		if len(item) > 1 and item[0] ==item[-1]:
			outputCount+=1
	return outputCount
	


def main():
	inp = input("Enter strings :")
	inplist = inp.split(",")
	output = perform(inplist)
	print(output)
	

if __name__ == '__main__':
	main()
	
	
# To create a copy or clone of a list inplis, simply use inplis2 = list(inplis)
