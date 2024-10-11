numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
primes = []
for i, j in enumerate(numbers):
    if j < 2:
        continue
    is_prime = True
    for k in range(2, j):
        if j % k == 0:
            not_primes.append(j)
            is_prime = False
            break
    if is_prime:
        primes.append(j)
print(primes)
print(not_primes)
