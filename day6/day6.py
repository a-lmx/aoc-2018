# https://adventofcode.com/2018/day/6

# Infinite: coordinates with the lowest or highest x or y values

# Put all pairs in a list
# determine largest x and y
# create grid sized by largest x and y
# for each location in grid:
#   calculate Manhattan distance to each coordinate, see what it's closest to
#   add location to list in dict keyed to coordinate
# sort dict by len(value)
#   find longest non-infinite

import sys

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def manhattan_distance(self, location2):
        return abs(self.x - location2.x) + abs(self.y - location2.y)

    def __repr__(self):
        return f'({self.x}, {self.y})'

class Grid:
    def __init__(self, max_x, max_y, coords):
        self.max_x = max_x
        self.max_y = max_y
        self.coords = coords

    def find_closest_coord(self, location):
        closest_distance = float('inf')
        closest_coords = []
        for coord in self.coords.keys():
            print(coord)
            distance = coord.manhattan_distance(location)
            print(distance)
            if distance == closest_distance:
                closest_coords.append(coord)
            if distance < closest_distance:
                closest_distance = distance
                closest_coords = [coord]    # clear out old coordinates
        if len(closest_coords) == 1:
            print(f'Closest coord is: {closest_coords[0]}')
            return closest_coords[0]
        else:   # two or more equidistant coordinates
            print('No single closest coord')
            return None
    
    def determine_areas(self):
        for x in range(self.max_x + 1):
            for y in range(self.max_y + 1):
                loc = Location(x, y)
                closest_coord = self.find_closest_coord(loc)
                if closest_coord:
                    self.coords[closest_coord].append(loc)
    
    def find_largest_area(self):
        coords_with_largest_area = []
        size_of_largest_area = 0
        for coord, locs in self.coords.items():
            if len(locs) >= size_of_largest_area:
                coords_with_largest_area.append(coord)
                size_of_largest_area = len(locs)
        print(f'The largest area is {coords_with_largest_area} with size {size_of_largest_area}')
        return coords_with_largest_area

        # TODO exclude infinite areas


def create_grid(filename):
    coordinates = open(filename).readlines()
    max_x = 0
    max_y = 0
    coords = {}
    for coord in coordinates:
        x, y = coord.split(', ')
        x = int(x)
        y = int(y)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        coords[Location(x, y)] = []
    return Grid(max_x, max_y, coords)

def main(filename):
    grid = create_grid(filename)
    grid.determine_areas()
    grid.find_largest_area()

main(sys.argv[1])
