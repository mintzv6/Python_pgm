'''def print_divisors(n):
	print("The divisors of",n,"are:")
	for i in range(1,n+1):
		if n%i==0:
			print(i)

num=int(input("Enter the Number:"))
print_divisors(num)

'''
def print_divisors(n):
	print("The divisors of",n,"are:")
	list=[]
	for i in range(1,n+1):
		if n%i==0:
			list.append(i)
	print(list)

num=int(input("Enter the Number:"))
print_divisors(num)