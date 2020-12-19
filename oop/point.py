import numpy as np

class Point3D:  # class name is Capital
    """Class point"""

    printed_rep = "*"

    def __init__(self, x: int = 0, y: int = 0, z: int = 0) :
        print('Initialized Point3D')
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """override str method. print the value of the point"""
        return "x = {} \ny = {} \nz = {}".format(self.x, self.y, self.z)

    def getX(self):
        """methods are function within the object and they always have at least one input, i.e., self"""
        return self.x

    def getY(self):
        """methods are function within the object and they always have at least one input, i.e., self"""
        return self.y

    def getZ(self):
        """methods are function within the object and they always have at least one input, i.e., self"""
        return self.z

    def getNorm2(self):
        """Compute the euclidean norm"""
        return np.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        """internal function which allow sum of two points e,g. p1(1,2,3) + p2(3,4,5)
        :type other: object
        """
        return Point3D(self.x + other.x,
                       self.y + other.y,
                       self.z + other.z)

    def avg(self, other):
        """method: compute average"""
        avg_x = (self.x + other.x)/2
        avg_y = (self.y + other.y)/2
        avg_z = (self.z + other.z)/2
        return Point3D(avg_x, avg_y, avg_z)

    def graph(self):
        """method: compute graph"""
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size - 1):
            if (j + 1) == int(self.y):
                special_row = str((j + 1) % 10) + (" " * (int(self.x) - 1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j + 1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)

p1 = Point3D(x=-1, y=-2, z=-3)
print(p1)

p2 = Point3D(x=1, y=2, z=3)
print(p2)

print(p1 + p2)

print(p1.avg(p2))

print(p2.graph())