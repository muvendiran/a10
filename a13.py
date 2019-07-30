p=int(input())
if p>1:
	for d in range(2,p):
		if(p%d==0):
			print("no")
			break
	else:
		print("yes")
else:
	print("no")
