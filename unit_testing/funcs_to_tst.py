# funcs_to_tst.py

def sentence(Name, place, time):
    return f'{Name} will go to the {place} at {time}.'

# Python Program to find Surface Area of a Cube.
# Surface Area of a Cube = 6l² (Where l is the Length of any side of a Cube).
# Area of a square = l².
# Since the Cube is made of 6 equal squares, Surface Area of a Cube = 6l².
def surface_area_cube(length):
	# sa = 6 * (length * length)
	# print("\n Surface Area of Cube = %.2f" %sa)
    return 6 * (length * length)

# Python Program to find Volume of a Cube.
def volume_cube(length):
	# Volume = length * length * length
	# print(" Volume of cube = %.2f" %Volume)
	return length * length * length

def registration(name,age):
    if age >= 18:
        return (name, age)
    else:
        return 'Not old enough to register!'
