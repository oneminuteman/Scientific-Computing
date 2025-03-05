import sympy as sp

s = sp.Symbol('s')

H_s = 1 / (s**2 + 3*s + 2)

denominator = s**2 + 3*s + 2
factored_denominator = sp.factor(denominator)
print("Factored Denominator:", factored_denominator)

t = sp.Symbol('t')
h_t = sp.inverse_laplace_transform(H_s, s, t)
print("Inverse Laplace Transform, h(t):", h_t)

poles = sp.solve(denominator, s)
print("Poles of the system:", poles)
