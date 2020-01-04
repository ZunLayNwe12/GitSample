#SETs

#includes a data type for sets.
#curly braces or the set () function can be used to create sets.


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

{'apple', 'pear', 'banana', 'orange'}      # remove the duplicate

pple', 'pear', 'banana', 'orange'}
'orange' in basket
True
'mango' in basket
False

a = set('abracadabra')
b = set('alacazam')
a
a - b      # a difference b          # in a not in b
a | b      # a union b               # in a or b or both
a & b      # a interset b            # in both a and b
a ^ b      # all - (a interset b)    # in a or b but not both a and b

a = {x for x in 'abracadabra' if x not in 'abc'}
a



fruits = {"apples", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

fruits.add("cucumber")
fruits

fruits.update("banana")
fruits
{'mango', 'b', 'apples', 'kiwi', 'a', 'melon', 'n', 'cherry', 'orange'}


fruits.remove("banana")
fruits
#{'mango', 'apples', 'kiwi', 'melon', 'cherry', 'orange'}

fruits.discard("kiwi")
fruits
#{'mango', 'apples', 'melon', 'cherry', 'banana', 'orange'}


>>>Dictionaries

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']
del tel['sape']
tel['irv'] = 4127
tel
#{'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)

sorted(tel)

'guido' in tel
'sape' in tel

dict([('sape', 4139), ('guido', 4127), ('jack', 4089)])
#  {'sape': 4139, 'guido': 4127, 'jack': 4089}


{x: x**2 for x in (2, 4, 6)}
{x: x**3 for x in (1, 2, 3, 4, 5)}

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():       # k is for index v is for value
	print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):     #it gives the number for each
	print(i, v)

	
questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('Whtat is your {0}? It is {1}.'.format(q, a))
