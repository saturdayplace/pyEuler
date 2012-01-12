def fibs(limit):
	""" Calculate the Fibbonacci numbers up to a given limit"""
	a, b = 0, 1
	while a < limit:
		yield a
		a, b = b, a + b
		

def factors_of(num):
	# A generator for gettting all the factors
	def generate_factors(num):
		limit = int(num/2)
		i = 1
		while i <= limit:
			if num % i == 0:
				yield i
			i += 1
	
	# Create a list from the generator
	return [i for i in generate_factors(num)]


def prime_factors_of(num):
	from primes import PRIMES
	factors = []
	
	if num == 1:
		return [1]
	
	for i in PRIMES:
		while True:
			if num % i == 0:
				factors.append(i)
				num /= i
			else:
				break

	return factors
		

def is_prime(num):
	if num == 1:
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
	
def is_palindrome(num):
	if str(num) == str(num)[::-1]:
		return True
	return False