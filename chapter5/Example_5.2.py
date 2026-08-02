
from dataclasses import asdict, dataclass, fields
from typing import NamedTuple
class Coordinate(NamedTuple):
    lat:float
    lon:float

    def __str__(self):
        ns='N' if self.lat>=0 else 'S'
        we='E' if self.lon>=0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


@dataclass
class Point:
    x:int
    y:int=0

p=Point(10)
p.y=20

print(asdict(p))
print([f.name for f in fields(p)])
print([f.default for f in fields(p)])

