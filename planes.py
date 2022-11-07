import math


class CartesianPlane:
    def __init__(self, x=0, y=0, z=0, d=0):
        self.x = x
        self.y = y
        self.z = z
        self.d = d

    def array(self):
        return [self.x, self.y, self.z, self.d]

    def pr_str(self):
        return str(self.x) + "x + " + str(self.y) + "y + " + str(self.z) + "z = " + str(self.d)
