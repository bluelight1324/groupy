import sympy as sp
from sympy.solvers.ode import infinitesimals

import sympy as sp

# Define the variables and function
x, y = sp.symbols('x y')
f = sp.Function('f')(x)

# Define the differential equation, e.g., dy/dx = y
diff_eq = sp.Eq(f.diff(x), f)

# Find the symmetries of the differential equation
symmetries = infinitesimals(diff_eq, func=f)

# Print the symmetries
print("Symmetries of the differential equation:")
for sym in symmetries:
    print(sym)

    # Print the symmetries as a table
sp.pretty_print(symmetries)
# Determine the group character (for simplicity, we will just list the symmetries)
group_character = [sym for sym in symmetries]

print("\nGroup character of the differential equation:")
for char in group_character:
    print(char)
