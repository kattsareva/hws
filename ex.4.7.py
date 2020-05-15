def gen():
    x = 1
    for el in range(1, 16):
        x *= el
        yield x

for el in gen():
    print(el)