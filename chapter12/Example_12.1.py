import functools
import operator
from array import array
import reprlib
import math

class Vector:
    typecode='d'
    __match_args__=('x','y','z','t')


    def __init__(self,components):
        self._components=array(self.typecode,components)


    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)])+bytes(self._components)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        if(isinstance(key,slice)):
            cls=type(self)
            return cls(self._components[key])
        index=operator.index(key)
        return self._components[index]

    def __getattr__(self, item):
        cls=type(self)
        try:
            pos=cls.__match_args__.index(item)
        except ValueError:
            pos=-1
        if 0<=pos<=len(self._components):
            return self._components[pos]
        msg=f"{cls.__name__!r} object has no attribute {item!r}"
        raise AttributeError(msg)

    def __setattr__(self, key, value):
        cls=type(self)
        if(len(key))==1:
            if key in cls.__match_args__:
                error='readonly attribute {attr_name!r}'
            if key.islower():
                error="can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error=""
            if error:
                msg=error.format(cls_name=cls.__name__,attr_name=key)
                raise AttributeError(msg)
            super().__setattr__(key,value)


    def __hash__(self):
        hashes=map(hash,self._components)
        return functools.reduce(operator.xor,hashes,0)


    # def __eq__(self, other):
    #     if(len(self)!=len(other)):
    #         return False
    #     for a,b in zip(self,other):
    #         if(a!=b):
    #             return False
    #     return True

    def __eq__(self, other):
        return len(self)==len(other) and all(a==b for a,b in zip(self,other))













v1 = Vector([3, 4, 5])
print(len(v1))

print(v1[0])

print(v1[-1])

v7=Vector(range(7))

print(v7)

print(v7[1:4])
print(v7[1,2])
v1.x=10
print(v1)
