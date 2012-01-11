from utils import is_palindrome

palindromes = []

for i in range(100, 1000):
	for j in range(100, 1000):
		num = i * j
		if is_palindrome(num):
			palindromes.append(num)
			
print sorted(palindromes)[-1]
		