multi = []
for i in range(1000):
    if i %3 == 0 or i %5 == 0:
        multi.append(i)
sum_multi = sum(multi)
print("The sum of all multiples of 3 and 5 below 1000 is:", sum_multi)

a, b = 1, 2
total = 0

while a <= 4_000_000:
    if a % 2 == 0:
        total += a
    
    a, b = b, a + b

print("The sum of all even Fibonacci numbers below 4 million is :", total)

n = 600851475143
d = 2

while d * d <= n:
    if n % d == 0:
        n //= d
    else:
        d += 1

print("Largest prime factor:", n)  
