
import sympy as sp
from sympy.combinatorics import PermutationGroup, Permutation

# Define the polynomial
x = sp.symbols('x')
polynomial = x**2 - 3*x + 1

# Find the roots of the polynomial
roots = sp.roots(polynomial, x)

# Extract the roots as a list
root_list = list(roots.keys())

# Define the permutations of the roots
permutations = []
for i in range(len(root_list)):
    for j in range(i + 1, len(root_list)):
        perm = list(range(len(root_list)))
        perm[i], perm[j] = perm[j], perm[i]
        permutations.append(Permutation(perm))

# Create the permutation group
symmetric_group = PermutationGroup(permutations)

# Output the symmetric group
print("The symmetric group of the polynomial is:")
print(symmetric_group)
