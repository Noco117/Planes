import math


class CartesianPlane:
    def __init__(self, x=0, y=0, z=0, d=0):
        self.x = x
        self.y = y
        self.z = z
        self.d = d

    def array(self):
        return [self.x, self.y, self.z, self.d]

    def parametric_form(self):
        pass

    def __repr__(self):
        return str(self.x) + "x + " + str(self.y) + "y + " + str(self.z) + "z = " + str(self.d)


class ParametricPlane:
    def __init__(self, holdVec, dirVec1, dirVec2):
        self.hV = holdVec
        self.dV1 = dirVec1
        self.dV2 = dirVec2

    def __repr__(self):
        return f"{self.hV} + t*{self.dV1} + s*{self.dV2}"
