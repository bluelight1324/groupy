import sympy as sp
from sympy.vector import CoordSys3D, curl

def faraday_law_symmetries():
    """
    Analyzes the Lie group symmetries of Faraday's Law.

    Faraday's Law in differential form is given by:
    curl(E) = -?B/?t

    This function sets up the components of the electric and magnetic fields
    and expresses Faraday's Law in component form.

    Returns:
        sympy.Eq: The component form of Faraday's Law.
    """
    # Define the coordinate system
    N = CoordSys3D('N')

    # Define the electric and magnetic fields as vector fields
    t = sp.symbols('t')
    E_x = sp.Function('E_x')(N.x, N.y, N.z, t)
    E_y = sp.Function('E_y')(N.x, N.y, N.z, t)
    E_z = sp.Function('E_z')(N.x, N.y, N.z, t)
    B_x = sp.Function('B_x')(N.x, N.y, N.z, t)
    B_y = sp.Function('B_y')(N.x, N.y, N.z, t)
    B_z = sp.Function('B_z')(N.x, N.y, N.z, t)

    E = E_x * N.i + E_y * N.j + E_z * N.k
    B = B_x * N.i + B_y * N.j + B_z * N.k

    # Faraday's Law in differential form
    faraday_law = sp.Eq(curl(E), -B.diff(t))

    return faraday_law

# Example usage
#if __name__ == "__main__":
    law = faraday_law_symmetries()
    sp.pretty_print(law)
