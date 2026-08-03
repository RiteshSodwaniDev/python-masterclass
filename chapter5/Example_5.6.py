from collections import namedtuple

Coordinate=namedtuple('Coordinate','lan lon reference',defaults=['WGS84'])
coordinate=Coordinate(0,0)
print(coordinate)
print(coordinate._field_defaults)


