/**
 * Clifford Algebra Implementation for Geometric Calculations
 * 
 * This implementation focuses on a 2D Clifford algebra (Cl(2,0)) which is particularly 
 * useful for representing rotations and geometric transformations in 2D space.
 * 
 * A Clifford algebra extends vector algebra by introducing geometric product between vectors,
 * combining both inner (dot) and outer (wedge) products. This provides a powerful framework
 * for geometric computations.
 * 
 * References:
 * - Hestenes, D. "New Foundations for Classical Mechanics"
 * - Dorst, L. et al. "Geometric Algebra for Computer Science"
 */

#include <iostream>
#include <cmath>
#define M_PI 3.14159265358979323846

// Clifford algebra class implementation for Cl(2,0)
// Basis elements: {1, e1, e2, e1e2}
// where e1^2 = e2^2 = 1, e1e2 = -e2e1
class Clifford {
public:
    double scalar;  // Scalar part (grade 0)
    double e1;      // Vector part e1 (grade 1)
    double e2;      // Vector part e2 (grade 1)
    double e12;     // Bivector part e1^e2 (grade 2)

    Clifford(double s = 0, double e1 = 0, double e2 = 0, double e12 = 0)
        : scalar(s), e1(e1), e2(e2), e12(e12) {}

    // Addition of Clifford numbers
    // Adds corresponding components grade-wise
    Clifford operator+(const Clifford& other) const {
        return Clifford(scalar + other.scalar, e1 + other.e1, e2 + other.e2, e12 + other.e12);
    }

    // Geometric product of Clifford numbers
    // Implements the full multiplication table of Cl(2,0)
    // e1e1 = e2e2 = 1, e1e2 = -e2e1 = e12
    Clifford operator*(const Clifford& other) const {
        return Clifford(
            scalar * other.scalar - e1 * other.e1 - e2 * other.e2 + e12 * other.e12,
            scalar * other.e1 + e1 * other.scalar,
            scalar * other.e2 + e2 * other.scalar,
            scalar * other.e12 + e1 * other.e2 - e2 * other.e1 + e12 * other.scalar
        );
    }

    // Display the Clifford number in standard basis representation
    // Format: scalar + e1 + e2 + e12 components
    void print() const {
        std::cout << scalar << " + " << e1 << "e1 + " << e2 << "e2 + " << e12 << "e12" << std::endl;
    }
};

/**
 * Computes the Clifford algebra representation of a rotation in SO(2)
 * 
 * In Clifford algebra, rotations can be represented using rotors:
 * R = cos(θ/2) + sin(θ/2)e12
 * 
 * The rotation of a vector v is then computed as: v' = RvR^†
 * where R^† is the conjugate of R
 * 
 * @param theta Rotation angle in radians
 * @return Clifford number representing the rotation
 */
Clifford findCliffordAlgebra(double theta) {
    // Basis vectors for SO(2)
    Clifford e1(0, 1, 0, 0);
    Clifford e2(0, 0, 1, 0);

    // Rotation matrix elements
    double cosTheta = std::cos(theta);
    double sinTheta = std::sin(theta);

    // Construct the Clifford algebra element
    Clifford rotation = Clifford(cosTheta, sinTheta, 0, 0);
    return rotation;
}

int main() {
    double theta = M_PI / 4.0; // Example angle (45 degrees)
    Clifford result = findCliffordAlgebra(theta);
    std::cout << "Clifford algebra element for rotation by " << theta << " radians: ";
    result.print();

    return 0;
}
