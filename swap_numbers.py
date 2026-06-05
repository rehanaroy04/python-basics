a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"\nBefore swapping: a = {a}, b = {b}")

(a, b) = (b, a)

print(f"After swapping: a = {a}, b = {b}")