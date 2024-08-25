
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator

def polynomial_approximation(func, degree, x_range):
    """
    Approximates a given function using a polynomial of specified degree.

    Args:
        func (callable): The input function to approximate.
        degree (int): The degree of the polynomial.
        x_range (tuple): The range of x values (min, max) for the approximation.

    Returns:
        tuple: The x values, the polynomial values, and the polynomial coefficients.
    """
    # Generate x values
    x = np.linspace(x_range[0], x_range[1], 1000)
    
    # Sample points for interpolation
    x_sample = np.linspace(x_range[0], x_range[1], degree + 1)
    y_sample = func(x_sample)
    
    # Create the polynomial interpolator
    interpolator = BarycentricInterpolator(x_sample, y_sample)
    
    # Evaluate the polynomial
    y_poly = interpolator(x)
    
    # Fit a polynomial to the sampled data points
    poly_coeffs = np.polyfit(x_sample, y_sample, degree)
    poly = np.poly1d(poly_coeffs)
    
    return x, y_poly, poly

def plot_function_and_polynomial(func, degree, x_range):
    """
    Plots the input function and its polynomial approximation.

    Args:
        func (callable): The input function to plot.
        degree (int): The degree of the polynomial.
        x_range (tuple): The range of x values (min, max) for the plot.
    """
    # Generate x values
    x = np.linspace(x_range[0], x_range[1], 1000)
    
    # Evaluate the input function
    y_func = func(x)
    
    # Get the polynomial approximation
    x_poly, y_poly, poly = polynomial_approximation(func, degree, x_range)
    
    # Print the polynomial coefficients
    print("Polynomial coefficients:", poly.coefficients)
    print("Polynomial:", poly)
    
    # Plot the input function
    plt.plot(x, y_func, label='Original Function', color='blue')
    
    # Plot the polynomial approximation
    plt.plot(x_poly, y_poly, label=f'Polynomial Approximation (degree={degree})', color='red', linestyle='--')
    
    # Add labels and legend
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Function and Polynomial Approximation')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Define the input function
    def input_function(x):
        return np.sin(np.cos(x))
    
    # Define the degree of the polynomial
    degree = 5
    
    # Define the range of x values
    x_range = (0, 2 * np.pi)
    
    # Plot the function and its polynomial approximation
    plot_function_and_polynomial(input_function, degree, x_range)
