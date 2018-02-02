n=int(input("Enter the no of inputs : "))
a=[input() for i in range(n)]
print("The no:s less than 5 are :\n")
for i in a:
	if int(i)<5:
		print(i)

