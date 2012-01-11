def fibs():
	a, b = 0, 1
	while a < 4000000:
		yield a
		a, b = b, a + b
	
fib_list = [i for i in fibs() if i % 2 == 0]
print sum(fib_list)