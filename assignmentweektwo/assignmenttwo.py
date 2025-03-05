import sympy as sp

A = sp.Matrix([[2, 1], [1, 3]])

det_A = A.det()
print("Determinant of A:", det_A)

λ = sp.Symbol('λ')
char_poly = A.charpoly(λ).as_expr()
print("Characteristic Polynomial:", char_poly)

eigenvalues = A.eigenvals()
eigenvalues_list = list(eigenvalues.keys())  # Extract eigenvalues
print("Eigenvalues of A:", eigenvalues_list)

for eigenvalue in eigenvalues_list:
    substituted = sp.simplify(char_poly.subs(λ, eigenvalue))  # Ensure simplification
    print(f"Substituting λ = {eigenvalue} into characteristic equation:", substituted)
    assert substituted == 0, "Error: Eigenvalue does not satisfy characteristic equation!"

print("All eigenvalues correctly satisfy the characteristic equation.")
