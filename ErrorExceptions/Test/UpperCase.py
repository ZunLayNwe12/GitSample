def find_lower(word):
	i = 0
	while not word[i].isupper():
		i = i+1
	return i
	print(find_lower('ABcDE'))