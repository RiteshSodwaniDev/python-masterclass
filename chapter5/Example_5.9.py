import typing
class Coordinate:
    lat:float
    lon:float

    def __init__(self,lat:float,lon:float):
        self.lat=lat
        self.lon=lon

trash=Coordinate('Ni!',None)
print(trash)