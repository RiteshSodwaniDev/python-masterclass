import numpy as np
a=np.arange(12)
print(a)

print(type(a))
print(a.shape)
a=a.reshape(3,4)
print(a)
print(a[2])

print(a[2,1])
print(a[:,1])
print(a.transpose())

t=(1,2,3,4)

try:
    print(hash(t))
    print(t)
except TypeError as e:
    print(e)

