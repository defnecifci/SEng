accurate_pi = 3.141592653589

def leibnitz_pi(n):
    pi = 0
    for i in range(n + 1):
        # Using (-1)**i correctly alternates the sign: +, -, +, -, ...
        sign = (-1) ** i
        pi += sign * 1 / (2 * i + 1)
    return pi * 4

# --- Leibniz Pi Loop Fix ---
diff = 0.0001
i = 0
while abs(leibnitz_pi(i) - accurate_pi) > diff:
    i += 1
print(f"Leibniz iterations needed for {diff}: {i}")


def euler_pi(n):
    pi = 0
    for i in range(1, n + 1):
        pi += 1 / (i * i)
    return (pi * 6) ** 0.5

print(f"Euler pi (n=10): {euler_pi(10)}")

# --- Euler Pi Loop ---
diff = 0.0001
i = 1
while abs(euler_pi(i) - accurate_pi) > diff:
    i += 1
print(f"Euler iterations needed for {diff}: {i}")