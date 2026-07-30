cafe = bytes('café', encoding='utf_8')

print(cafe)
print(cafe[0])
print(cafe[0:1])

cafe_arr=bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])
