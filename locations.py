from math import sqrt

example_locations = {"london": (0, 0),
                     "york": (100, 200),
                     "manchester": (-100, 200),
                     "edinburgh": (100, 500)}

max_distance = max([sqrt(location[0]**2 + location[1]**2) for location in example_locations.values()])

