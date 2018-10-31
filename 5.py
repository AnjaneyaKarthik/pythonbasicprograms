#. Write a Python function that takes two lists and returns True if they have at least one common member.


def perform(list1,list2):
	outlist = list(set(list1) & set(list2))
	if outlist:
		out = "True"
		return True
	else:
		return False
	


def main():
	inp1 = input("Enter numbers") # Ask for input if any
	inp2 = input("Enter numbers")
	list1 = inp1.split(",")
	list2 = inp2.split(",")
	output = perform(list1,list2)
	print(output)


if __name__ == '__main__':
	main()
	
	
	
'''
Key Points

using set operations on the list (union, intersection etc.,)


'''