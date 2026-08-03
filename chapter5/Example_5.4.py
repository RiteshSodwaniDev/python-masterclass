from collections import namedtuple
import json

City=namedtuple('City','name country population coordinates')

tokyo=City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
print(City._fields)
Coordinate=namedtuple('Coordinate','lat lon')
delhi_data=('Delhi NCR','IN',21.935,Coordinate(28.613889,77.208899))
delhi=City._make(delhi_data)
print(delhi._asdict())
print(json.dumps(delhi._asdict()))

