using System;
using Python.Runtime;

class Program
{
    static void Main()
    {
        // Initialize the Python runtime
        PythonEngine.Initialize();

        using (Py.GIL())
        {
            dynamic sympy = Py.Import("sympy");
            dynamic lie = Py.Import("sympy.solvers.ode.lie_group");

            // Define the differential equation directly using SymPy
            dynamic f = sympy.Function("dy/dx=0");
            dynamic x = sympy.Symbol("x");
            dynamic eq = sympy.Eq(f(x).Diff(x, x) - f(x), 0);

            // Find the Lie group
            dynamic lie_group = lie.infinitesimals(eq, f(x), x);

            // Print the result
            Console.WriteLine("Lie group of the differential equation:");
            Console.WriteLine(lie_group);
        }

        // Shutdown the Python runtime
        PythonEngine.Shutdown();
    }
}
