a=int(input())
b=[]
for i in range(a):
	c=int(input())
	b.append(c)
for i in range(a):
	if (i%2==0):
		print(b[i],end=' ')