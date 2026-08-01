from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
    lat:float
    lon:float

    def __str__(self):
        ns='N' if self.lat>=0 else 'S'
        we='W' if self.lon>=0 else 'E'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
