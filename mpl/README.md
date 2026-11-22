## MPL FILE
- Leibniz
- Fibonacci
- Euler
- Wallis

# Pi Approximation: Leibniz vs. Euler vs. Wallis

A simple Python script that compares the convergence rates of three classic mathematical formulas for approximating π: the **Leibniz formula**, **Euler's solution to the Basel problem**, and the **Wallis product**.

## Features

- **Leibniz Formula for π**: Uses an alternating series (\(\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots\)). *Note: This method converges very slowly.*
- **Euler's Formula (Basel Problem)**: Uses reciprocal squares (\(\frac{\pi^2}{6} = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \dots\)). *Note: This converges faster than the Leibniz series.*
- **Wallis Product**: Uses an infinite product to approximate π. *Note: This method also converges slowly.*
- **Iteration Counter**: Automatically calculates how many iterations are needed for each method to reach a target precision (`diff = 0.0001`).

## Python Code

```python
accurate_pi = 3.141592653589

def leibnitz_pi(n):
    pi = 0
    for i in range(n + 1):
        # Using (-1)**i correctly alternates the sign: +, -, +, -, ...
        sign = (-1) ** i
        pi += sign * 1 / (2 * i + 1)
    return pi * 4

# --- Leibniz Pi Loop ---
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


def wallis_pi(n):
    product = 1.0
    for i in range(1, n + 1):
        term = ((2.0 * i) / (2.0 * i - 1.0)) * ((2.0 * i) / (2.0 * i + 1.0))
        product *= term
    return product * 2.0

# --- Wallis Pi Loop ---
diff = 0.0001
i = 1
while abs(wallis_pi(i) - accurate_pi) > diff:
    i += 1
print(f"Wallis iterations needed for {diff}: {i}")
```