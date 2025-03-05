import sympy as sp

x = sp.Symbol('x')

L = 3*x**2 + 2*x - 5
L_derivative = sp.diff(L, x)
print("Gradient (First Derivative):", L_derivative)

critical_points = sp.solve(L_derivative, x)
print("Critical Points:", critical_points)

L_second_derivative = sp.diff(L_derivative, x)
print("Second Derivative:", L_second_derivative)

for point in critical_points:
    if L_second_derivative.subs(x, point) > 0:
        print(f"x = {point} is a Minimum (Second derivative is positive)")
    elif L_second_derivative.subs(x, point) < 0:
        print(f"x = {point} is a Maximum (Second derivative is negative)")
    else:
        print(f"x = {point} is an Inflection Point (Second derivative is zero)")
