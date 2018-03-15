f = open("uploads/users.txt", "r")
t = [line.split(',') for line in f.readlines()]

for li in t:
	k="Name:"+li[0]+"\n"+"E-mail:"+li[1]
	print (k)

f.close()


