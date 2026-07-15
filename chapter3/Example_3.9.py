import collections
class StrkeyDict0(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)]=value



d = StrkeyDict0([
    ('2', 'two'),
    ('4', 'four'),
])

print(d)

print(d['2'])
print(d[2])
d[1]="One"
print(d)