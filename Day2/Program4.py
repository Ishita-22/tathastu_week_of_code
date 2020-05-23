n=5
for i in range(1,n+1):
	print('*'*(n-i+1)+" "*2*i+'*'*(n+1-i))
for i in range(1,n+1):
	print("*"*i+" "*2*(n+1-i)+'*'*i)
