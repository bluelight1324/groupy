import sympy as sp
from sympy.solvers.ode import infinitesimals
from sympy.vector import CoordSys3D, curl

# Define the coordinate system
N = CoordSys3D('N')

# Define the electric and magnetic fields as vector fields
E = sp.Function('E')(N.x, N.y, N.z, sp.symbols('t')) * N.i + \
    sp.Function('E')(N.x, N.y, N.z, sp.symbols('t')) * N.j + \
    sp.Function('E')(N.x, N.y, N.z, sp.symbols('t')) * N.k
B = sp.Function('B')(N.x, N.y, N.z, sp.symbols('t')) * N.i + \
    sp.Function('B')(N.x, N.y, N.z, sp.symbols('t')) * N.j + \
    sp.Function('B')(N.x, N.y, N.z, sp.symbols('t')) * N.k

# Faraday's Law in differential form
faraday_law = sp.Eq(curl(E), -B.diff(sp.symbols('t')))

# Find the symmetries of Faraday's Law
#symmetries = infinitesimals(faraday_law, func=E)

# Print the symmetries
sp.pretty_print(faraday_law )

