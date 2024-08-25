#include <iostream>
#include <cmath>

// Define a simple Clifford algebra class
class Clifford {
public:
    double scalar;
    double e1;
    double e2;
    double e12;

    Clifford(double s = 0, double e1 = 0, double e2 = 0, double e12 = 0)
        : scalar(s), e1(e1), e2(e2), e12(e12) {}

    // Addition
    Clifford operator+(const Clifford& other) const {
        return Clifford(scalar + other.scalar, e1 + other.e1, e2 + other.e2, e12 + other.e12);
    }

    // Multiplication
    Clifford operator*(const Clifford& other) const {
        return Clifford(
            scalar * other.scalar - e1 * other.e1 - e2 * other.e2 + e12 * other.e12,
            scalar * other.e1 + e1 * other.scalar,
            scalar * other.e2 + e2 * other.scalar,
            scalar * other.e12 + e1 * other.e2 - e2 * other.e1 + e12 * other.scalar
        );
    }

    // Print the Clifford number
    void print() const {
        std::cout << scalar << " + " << e1 << "e1 + " << e2 << "e2 + " << e12 << "e12" << std::endl;
    }
};

// Example Lie group: SO(2) rotation
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
    double theta = 180/ 4; // Example angle (45 degrees)
    Clifford result = findCliffordAlgebra(theta);
    std::cout << "Clifford algebra element for rotation by " << theta << " radians: ";
    result.print();

    return 0;
}
