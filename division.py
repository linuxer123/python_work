import json
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")
	
try:
	a=['a','b']
	b={"tt":"hello"}
	filename="d:/Users/Desktop/1234.txt"
	with open(filename, 'a') as fobj:
		json.dump(b, fobj)
except FileNotFoundError:
	pass
else:	
	pass
	
	

	
	
