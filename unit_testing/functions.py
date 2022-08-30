def adder(x, y):
    return x + y

def subber(x, y):
    return x - y

def make_list(x,y,z):
    list = []
    list.extend([x,y,z])
    return x+1,y+1,z+1

def divider(x,y):
    if y == 0:
        raise ValueError('Tried to divide by 0.')
    return x/y

def startup():
    result = make_list(1,2,3)
    print(type(result))

startup()