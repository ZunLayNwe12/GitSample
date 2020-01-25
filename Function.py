print(print_max.__doc__)
def paper():
	'''1. There will be situations where your
	program has to interact with the user.
	For example, you would want to take input 
	from the user and then print saome results
	back. We can achieve this using the input()
	function and print function respectively. '''

	'''2. There will be situations where your
	program has to interact with the user.
	For example, you would want to take input 
	from the user and then print saome results
	back. We can achieve this using the input()
	function and print function respectively. '''

print(paper.__doc__)


#DocString (Documentation Strings)

def print_max(x, y):
	'''Print the maximum of two numbers 
		The two values must be integers.
	'''

	x = int(x)
	y = int(y)

	if x > y :
		print(x, 'is maximum')

	elif x < y:
		print(y, 'is maximum')
	else:
		print(x, '&', y, 'is equal')

print_max(5,9)

print(print_max.__doc__)

def paper():

