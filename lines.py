import math
import sympy as sp
from fractions import Fraction


class CartesianLine:
    def __init__(self, x0, a, y0, b, z0, c):
        self.x0 = x0
        self.a = a
        self.y0 = y0
        self.b = b
        self.z0 = z0
        self.c = c

    def __repr__(self):
        return f"E: (x - {self.x0})/{self.a} = (y - {self.y0})/{self.b} = (z - {self.z0})/{self.c}"

    def to_parametric_line(self):
        x_com = [self.x0, self.a]
        y_com = [self.y0, self.b]
        z_com = [self.z0, self.c]

        return ParametricLine([x_com[0], y_com[0], z_com[0]], [x_com[1], y_com[1], z_com[1]])



class ParametricLine:
    def __init__(self, holdvec, dirvec):
        self.hV = holdvec
        self.dV = dirvec

    def __repr__(self):
        return f"E: v = {self.hV} + t*{self.dV}"

    def to_cartesian_line(self):
        return CartesianLine(self.hV[0], self.dV[0], self.hV[1], self.dV[1], self.hV[2], self.dV[2])
