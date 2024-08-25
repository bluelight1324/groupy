
import sympy as sp

def describe_sphere(n):
    # Define the variables for the n+1 dimensional space
    coords = sp.symbols(f'x1:{n+2}')
    
    # Define the equation of the n-dimensional sphere in R^(n+1)
    sphere_eq = sum(x**2 for x in coords) - 1
    
    # Output the equation of the sphere
    print(f"The equation of the {n}-dimensional sphere S^{n} in R^{n+1} is:")
    sp.pprint(sphere_eq)

# Example: Describe a 2-dimensional sphere (S^2) in 3-dimensional space (R^3)
describe_sphere(2)
