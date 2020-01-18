# "r" - Read

# "a" - Append

# "w" - Write

# "x" - Create

# "t" - Text

# "b" - Binary

#open & read file

# f = open('test.txt','r') # r - read

# print(f.name)

# f.close()

# with open('test1.txt', 'a') as g:
# 	g.write('This is line number 6'+"\n")

# 	print(g,end='')


with open('test.txt','r') as f:
	# f_text = f.readline()
	# print(f_text,end='')

	# f_text = f.readline()
	# print(f_text,end='')

	# for line in f:
	# 	print(line,end='')

	# f_text = f.read(60)       #read the number of words (read only 60 characters)
	# print(f_text,end='')

	size_to_read = 100
	f_text = f.read(size_to_read)

	while len(f_text) > 0:
		print(f_text,end='')

	# f_text = f.read(100)             #the same as above

	# while 100 > 0:
	# 	print(f_text,end='')









