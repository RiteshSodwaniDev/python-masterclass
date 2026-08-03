from DemoClass import  DemoPlainClass
from DemoNTclass import DemoNTClass

print(DemoPlainClass.__annotations__)
print(DemoPlainClass.b)
print(DemoPlainClass.c)
#print(DemoPlainClass.a)

o=DemoPlainClass
print(o.b)
print(o.c)
#print(o.a)

print(DemoNTClass.a)
print(DemoNTClass.b)
print(DemoNTClass.c)

b=DemoNTClass(8)

print(b.a)
print(b.b)
print(b.c)

#b.a=12
