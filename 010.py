from utils import is_prime
from primes import PRIMES # prime numbers under 1,000,000.  Generated previously

for i in xrange(1000000,2000000): # Need to get the rest under 2,000,000
	if is_prime(i):
		PRIMES.append(i)
		
print sum(PRIMES)