# https://adventofcode.com/2018/day/6

import sys

class Location:
    def __init__(self, x, y, label=None):
        self.x = x
        self.y = y
        self.label = label

    def manhattan_distance(self, location2):
        return abs(self.x - location2.x) + abs(self.y - location2.y)

    def __repr__(self):
        return f'({self.x}, {self.y})'

class Grid:
    def __init__(self, min_x, max_x, min_y, max_y, coords, safe_distance=None):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.coords = coords
        self.border_coords = set()
        self.marked_grid = []
        if safe_distance:
            self.safe_distance = int(safe_distance)
        else:
            self.safe_distance = safe_distance

    def __repr__(self):
        return f'Grid:\nmin x: {self.min_x}, max_x: {self.max_x},\nmin_y: {self.min_y}, max_y: {self.max_y}'

    def find_safe_locations(self):
        num_safe_locations = 0
        for x in range(self.max_x + 1):
            for y in range(self.max_y + 1):
                sum_to_all_coords = 0
                loc = Location(x, y)
                for coord in self.coords:
                    sum_to_all_coords += coord.manhattan_distance(loc)
                    if sum_to_all_coords > self.safe_distance:
                        break
                if sum_to_all_coords < self.safe_distance:
                    num_safe_locations += 1
        print(f'There are {num_safe_locations} safe locations.')
        return num_safe_locations

    def find_closest_coord(self, location):
        closest_distance = float('inf')
        closest_coords = []
        for coord in self.coords:
            distance = coord.manhattan_distance(location)
            if distance == closest_distance:
                closest_coords.append(coord)
            if distance < closest_distance:
                closest_distance = distance
                closest_coords = [coord]    # clear out old coordinates
        if len(closest_coords) == 1:
            return closest_coords[0]
        else:   # two or more equidistant coordinates
            return None

    def draw_areas(self):
        self.marked_grid = [[0 for x in range(self.max_x + 1)] for y in range(self.max_y + 1)]
        for x in range(self.max_x + 1):
            for y in range(self.max_y + 1):
                loc = Location(x, y)
                closest_coord = self.find_closest_coord(loc)
                if closest_coord:
                    self.marked_grid[y][x] = closest_coord.label

    def record_infinite_areas(self):
        for x in self.marked_grid[0]:
            self.border_coords.add(x)
        for x in self.marked_grid[-1]:
            self.border_coords.add(x)
        for y in range(len(self.marked_grid)):
            self.border_coords.add(self.marked_grid[y][0])
            self.border_coords.add(self.marked_grid[y][-1])

    def count_areas(self):
        area_map = {}
        for y in range(len(self.marked_grid)):
            for x in range(len(self.marked_grid[0])):
                label = self.marked_grid[y][x]
                if label in area_map:
                    area_map[label] = area_map[label] + 1
                else:
                    area_map[label] = 1
        return area_map
    
    def find_largest_finite_area(self, area_map):
        largest_area_size = 0
        largest_area_label = []
        for label, size in area_map.items():
            if label in self.border_coords:
                continue
            else:
                if size == largest_area_size:
                    largest_area_label.append(label)
                elif size > largest_area_size:
                    largest_area_label = [label]
                    largest_area_size = size
        print(f'The largest finite area is {largest_area_label[0]} with size {largest_area_size}.')


class GridManager:
    def __init__(self, filename, safe_distance=None):
        coordinates = open(filename).readlines()
        max_x = 0
        max_y = 0
        min_x = float('inf')
        min_y = float('inf')
        coords = []
        label = 1
        for coord in coordinates:
            x, y = coord.split(', ')
            x = int(x)
            y = int(y)
            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x
            if y > max_y:
                max_y = y
            if y < min_y:
                min_y = y
            coords.append(Location(x, y, label))
            label += 1
        self.grid = Grid(min_x, max_x, min_y, max_y, coords, safe_distance)

    def minimize_danger(self):
        self.grid.draw_areas()
        self.grid.record_infinite_areas()
        area_map = self.grid.count_areas()
        self.grid.find_largest_finite_area(area_map)

    def maximize_safety(self):
        self.grid.find_safe_locations()

def main(filename, action, safe_distance=None):
    grid_manager = GridManager(filename, safe_distance)
    if action == 'danger':
        grid_manager.minimize_danger()
    if action == 'safety':
        grid_manager.maximize_safety()

if len(sys.argv) > 3:
    main(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    main(sys.argv[1], sys.argv[2])
