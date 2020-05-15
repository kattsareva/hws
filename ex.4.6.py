from itertools import count, cycle

def func():
    l = []
    ex = 0
    for el in count(5):
        if el > 10:
            break
        l.append(el)
    for i in cycle(1):
        if ex > 20:
            break
        ex += 1
        print(i)
        
func()