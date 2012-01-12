from utils import factors_of, is_prime

factors = factors_of(600851475143)

prime_factors = []

for fact in factors:
	if is_prime(fact):
		prime_factors.append(fact)
		
print sorted(prime_factors)[-1]