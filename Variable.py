#21.12.2019
>>> text = "This is a string"
>>> text
'This is a string'
>>> 2 + 2
4
>>> 50 - 5 * 6
20
>>> (50 - 5 * 6) / 4
5.0
>>> round(5.0)
5
>>> 5.123456
5.123456
>>> round(5.123456,2)
5.12
>>> 17 / 3           # division returns a float
5.666666666666667
>>> 17 // 3          # discards the fraction
5
>>> 17 % 3    # returns the remainder
2
>>> 17 * 4 % 3      # 1st * 2nd %
2
>>>
7 ** 3
343
>>> 3 ** 2       # 3 to the power of 2
9
a = 1
a (variable) = (assign) 1 (value)

width = 20 
height = 5 * 9
vol = width * height
vol

>>>4 * 3.75 - 1
14.0
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round (_, 2)
113.06
>>> sale = 30000
>>> tax = 5 / 100
>>> total_tax = sale * tax
>>> total_tax
1500.0
>>> total_price = sale + total_tax
>>> total_price
31500.0
>>>
print('spam eggs')
print('"Yes"')
print("\"Yes,\" they said.")
 

 s = 'First line.\nSecond line.'
>>> print(s)
First line.
Second line.
>>>

# \n  = new line

>>> print("""\
... Usage: thingy
...     -a
...     -b
...     -c
... """)
Usage: thingy
        -a
        -b
        -c

>>> 3 * 'un' + 'ium'
'unununium'
>>> 3 * 'A'
'AAA'
>>> 2 * 'BC' + 'DE'
'BCBCDE'
>>> 10 * 'GH' + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 'GH' + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 'GH' + '3'
'GH3'
>>> 10 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 2 * 'BC' - 'DE'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> 'Py' 'thon'
'Python'
>>>
word[3:5]
word[:5]
word[8:]
>>> word[8:]
'ing'
>>> word[-2:5]
''
>>> word[5:-3]
'amm'
>>> word[:2] + word[3:]
'Prgramming'




>>> List