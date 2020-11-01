def cb(x):
	if(x%2) == 0:
		print x
	else:
		print (x*x*x)

for i in range(20):
	x = i
	cb(x)
