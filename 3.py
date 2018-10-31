#Write a program to remove duplicates from a list


def perform(lis):
	set1 = set(lis)
	outlist = list(set1)
	return outlist
	


def main():
	inp = input("Enter numbers") # Ask for input if any
	inplist  = inp.split(",")
	outlist = perform(inplist)
	print(outlist)

if __name__ == '__main__':
	main()
	
	
'''
Keypoints

set is a datastructure which contains only unique elements. set(listname) converts list to set with unique values.


'''