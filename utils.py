def factors_of(num):
	limit = int(num**0.5)+1
	i = 1
	while i <= limit:
		if num % i == 0:
			yield i
		i += 1

def is_prime(num):
	if num < 2:
		return False
	
	if num == 2:
		return True
		
	if num % 2 == 0: # Evens are not
		return False
		
	# Test all the odd numbers between 3 and the square root of the number
	for x in xrange(3, int(num**0.5)+1, 2):
		if num % x == 0:
			return False
		
	return True