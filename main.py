import planes
import lines
import sympy as sp

sp.init_printing(use_unicode=True)
p1 = planes.CartesianPlane(3, 2, -2, -1)
p2 = planes.CartesianPlane(1, -4, -2, 9)



def intersect_cartesian_planes(p1, p2):
    if not (type(p1) == planes.CartesianPlane and type(p2) == planes.CartesianPlane):
        raise Exception("TypeError: Not a planes.CartesianPlane object")
    sol_mat = sp.nsimplify(sp.Matrix([p1.array(), p2.array()]).rref()[0], tolerance=0.001, rational=True)

    c = -1/sol_mat[0, :][-2]
    z = -c*sol_mat[0, :][-1]
    b = -c*sol_mat[1, :][-2]
    y = sol_mat[1, :][-1] + sol_mat[1, :][-2]*c

    cart_equation = lines.CartesianLine(x0=0, a=1, b=b, y0=y, c=c, z0=z)

    return cart_equation

print(intersect_cartesian_planes(p1, p2))