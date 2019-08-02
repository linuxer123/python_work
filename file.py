filename="d:/Users/Desktop/123.txt"
with open(filename) as file_object:
	contents=file_object.read()
	print(contents.rstrip())


with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

#放入队列
with open(filename) as file_object:
	lines=file_object.readlines()
	#for line in lines:
	#	print(line.rstrip("\n"))

	pi_lines=''
	for line in lines:
		pi_lines +=line.strip()
	print(pi_lines[:52]+'...')
	print(len(pi_lines))
#打开文体文件int float转换数字使用



