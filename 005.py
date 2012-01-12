"""
Get the Least Common Multiple of the numbers 1-20
"""

from utils import prime_factors_of

one_twenty = range(1,21)

factors = {}
greatest_powers = {}
lcm = 1

for i in one_twenty:
	factors[i] = prime_factors_of(i)
	
for num, factors in factors.items():
		
	for i in one_twenty:
		power_of_i = factors.count(i)
		greatest_power_of_i = greatest_powers.get(i)
		
		if greatest_power_of_i:
			if power_of_i > greatest_power_of_i:
				greatest_powers[i] = power_of_i
				
		else:
			greatest_powers[i] = power_of_i
			
for num, power in greatest_powers.items():
	lcm *= num**power
	
print lcm