def sentence(Name, place, time):
    return f'{Name} will go to the {place} at {time}.'

def surface_area_cube(x,y,z):
    return (2*x*y) + (2*x*z) + (2*y*z)

def registration(name,age):
    if age >= 18:
        return (name, age)
    else:
        return ''
