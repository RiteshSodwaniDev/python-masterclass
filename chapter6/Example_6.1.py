charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis=charles
print(lewis is charles)
print(id(lewis))
print(id(charles))
lewis['balance']=950
print(lewis)
print(charles)
alex={'name': 'Charles L. Dodgson', 'born': 1832, 'balance':950}
print(alex==charles)
print(alex is not charles)
print(id(alex))
print(id(charles))
