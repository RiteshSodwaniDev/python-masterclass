from coordinates import Coordinate
from collections import namedtuple
import typing


moscow=Coordinate(55.76,37.62)
print(moscow)
location=Coordinate(55.76,37.62)
print(location==moscow)
print((location.lat,location.lon)==(moscow.lat,moscow.lon))

coordinate1=namedtuple('Coordinate', 'lat lon')
print(issubclass(coordinate1,tuple))
moscow=coordinate1(55.756,37.617)
print(moscow)
print(moscow==coordinate1(lat=55.756,lon=37.617))


Coordinate=typing.NamedTuple('Coordinate',[('lat',float),('lon',float)])
print(issubclass(Coordinate,tuple))

print(typing.get_type_hints(Coordinate))

