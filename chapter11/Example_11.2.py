from array import array
import math

class vector2d:
    typecode='d'

    def __init__(self,x,y):
        self.__x=float(x)
        self.__y=float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.__x,self.__y))

    def __repr__(self):
        class_name=type(self).__name__
        return '{}({!r},{!r})'.format(class_name,*self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes(ord[self.typecode])+bytes(array(self.typecode,self)))

    def __eq__(self, other):
        return tuple(self)==tuple(other)

    def __hash__(self):
        return hash(self.x)^hash(self.y)

    def __abs__(self):
        return math.hypot(self.__x,self.__y)

    def __complex__(self):



    def __bool__(self):
        return bool(abs(self))


ob1=vector2d(3,4)




def is_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

print(is_hashable(ob1))