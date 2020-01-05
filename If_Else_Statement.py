print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))



Python Conditions

Equals                           ->     x == y
Not Equals                       ->     x != y
Less than                        ->     x <  y
Less than or equal to            ->     x <= y
Greater than                     ->     x >  y
Greater than or equal to         ->     x >= y
Boolean OR                       ->     x or y , x | y
Boolean AND                      ->     x and y , x & y
Boolean NOT                      ->     not x



# if statement


x = 70
y = 60
if x > y:
...     print("x is greater than y")


x = 70
y = 70
if x > y:
...     print("x is greater than y")
... elif x ==y:
...     print("x and y are equal")
...
#x and y are equal




x = 50
>>> y = 150
>>> if x > y:
...     print("x is greater than y")
... elif x == y:
...     print("x and y are equal")
... else:
...     print("x is less than y")
...
#x is less than y

#Short hand If

if x > y: print("x is greater than y")

x = 70
y = 50
if x > y: print("x is greater than y")
...
#x is greater than y (result)



#Short hand If...Else

x = 50
y = 150
print(x) if x > y else print(y)



#
x = 50
y = 40
z = 100
if x > y or z > x:
...     print("All conditions are True")
... else:
...     print("All conditions are False")
...
#All conditions are True



x = 50
y = 40
z = 100
if x > y and z > x:
...     print("All conditions are True")
... else:
...     print("All conditions are False")
...
#All conditions are True




x = 50
>>> y = 40
>>> z = 100
>>> if x > y and z > y:
...     print("All conditions are True")
... elif x > y or z > y:
...     print("One of the conditions is True")
... else:
...     print("nothing else")
...
#All conditions are True

#Nested If is If statements in if statements

x = 50
if x > 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
	else:
		print("No,x is not greater than 20")



#Pass statement
x = 100
y = 50
if x > y:
	pass


--------