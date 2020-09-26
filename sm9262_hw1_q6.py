import copy
class Vector:

    def __init__(self, d):
        if isinstance(d, list):
           self.coords = copy.deepcopy(d)
        else:
            self.coords = [0]*d;

    def __sub__(self, other):
        if(len(other) != len(self)):
            raise ValueError("dimension must agree")
        subtracted = Vector(len(other))
        for i in range(len(other)):
            subtracted[i] = self[i] - other[i]
        return subtracted

    def __neg__(self):
        return Vector([i*-1 for i in self]);


    def __mul__(self, other):
        if isinstance(other, Vector):
            if(len(other) != len(self)):
                raise ValueError("dimensions must agree")
            return sum([other[i]*self[i] for i in range(len(self))])

        else:
            return Vector([other*i for i in self])


    def __rmul__(self, other):
        return Vector([other*i for i in self])

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if(len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '<'+ str(self.coords)[1:-1] + '>'

    def __repr__(self):
        return str(self)






