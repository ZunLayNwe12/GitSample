22.12.2019

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


word = "Programming"
len(word)

#len = length

square = "Square"
len(square)
len(word) + len(square)

cube = [10, 20,]
cube = [10, 20, 30, 45, 50]
>>> cube
[10, 20, 30, 45, 50]
>>> cube[3] = 40
>>> cube
[10, 20, 30, 40, 50]
>>> cube[5] = 60               #index out of range

cube.append(60)
cube
[10, 20, 30, 40, 50, 60]

cube.append(4+10+20+36)
cube
[10, 20, 30, 40, 50, 60, 70]

programA = ['A','B','C','D','E']
programB = ['a','b','c','d','e']
programC =programA + programB
programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
>>> programD = [1, 2, 3, 4, 5]
>>> programC = programC + programD
>>> programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5]


programC[9:] = []       # from index9 are removed
programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd']

programC[5:9] = programD        #index 5 to 9 is replaced by programD
programC
['A', 'B', 'C', 'D', 'E', 1, 2, 3, 4, 5]

len(programC)
10

a = [10, 20, 30, 40, 50]
b = [60, 70, 80, 90, 100]
c = [110, 120, 130, 140, 150]
x = [a, b, c]
x
[[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]]

x[2][4]        #index2 from x and 
150

x[0][]
x[][3]
x[1][2]
x[][]
x[0][0]
x[1][1]
x[]

>>> x[1][2] + x[2][0]
190
>>> x[0][1] - x[2][1]
-100

>>> If else statement 