"""
Tutorial 1, Question 2.

Calculates 3 angles of a triangle. Optimized for single calculation.
Batch calculation will prefer using dot product instead of cosine law.
"""


import numpy as np


class TriangleAngle:
    """Output 3 angles from triangle."""

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.angle_a = None
        self.angle_b = None
        self.angle_c = None

    def get_angles(self):
        """Get angles from 3 sides."""

        sides = sorted([self.side_a, self.side_b, self.side_c])

        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Invalid Triangle Sides.")

        #Using cosine law, cos(A) = (B**2 + C**2 - A**2) / (2BC).
        cos_a = (self.side_b**2 + self.side_c**2 - self.side_a**2) / (2 * self.side_b * self.side_c)
        cos_b = (self.side_a**2 + self.side_c**2 - self.side_b**2) / (2 * self.side_a * self.side_c)

        #Clip required incase of f.p. error. 
        #E.g. cos_a = 1.000...1 will cause np.arccos to fail.
        self.angle_a = np.arccos(np.clip(cos_a,-1,1))
        self.angle_b = np.arccos(np.clip(cos_b,-1,1))
        self.angle_c = np.pi - self.angle_a - self.angle_b

        return 0
    

if __name__ == "__main__":
    triangle = TriangleAngle(3,7,9)
    triangle.get_angles()
    print(
        f"The angles of the triangle are: {triangle.angle_a:.2f}rads, "
        f"{triangle.angle_b:.2f}rads, {triangle.angle_c:.2f}rads"
    )

