filename="d:/Users/Desktop/123.txt"
with open(filename) as file_object:
	contents=file_object.read()
	print(contents.strip())
