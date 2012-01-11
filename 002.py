from utils import fibs
	
fib_list = [i for i in fibs(4000000) if i % 2 == 0]
print sum(fib_list)