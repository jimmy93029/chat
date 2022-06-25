lines = []
with open('3.txt','r',encoding = 'utf-8-sig') as file:
	for line in file:
		lines.append(line.strip().split(' '))
print(lines)

for text in lines:
	time = text[0][:5]
	name = text[0][5:]
	print(time)
	print(name)


