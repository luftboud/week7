"""looking for pirate's treasure"""
import math
def define_direction(previous_direction, azimuth):
    """
    Calculate the new path direction based on the current direction
    and the pirate's biased azimuth. The azimuth is given in degrees
    and can be any non-negative multiple of 90. The directions are 
    represented as 'N' for North, 'E' for East, 'S' for South, and 'W' 
    for West.

    Args:
    previous_direction (str): The current direction ('N', 'E', 'S', 'W').
    azimuth (int): The azimuth in degrees (non-negative multiple of 90).

    Returns:
    str: The new direction as a single character string.

    For example:
    - If the current direction is North ('N') and the azimuth is 90 degrees,
      the new direction will be East ('E').
    - If the current direction is South ('S') and the azimuth is 90 degrees,
      the new direction will be West ('W').

    >>> define_direction('W', 270)
    'S'
    >>> define_direction('N', 270)
    'W'
    >>> define_direction('N', 0)
    'N'
    >>> define_direction('N', 90)
    'E'
    >>> define_direction('N', 180)
    'S'
    >>> define_direction('E', 90)
    'S'
    """
    directions = ['N','E', 'S', 'W']
    index = directions.index(previous_direction)
    rotations = azimuth/90
    new_index = index + rotations
    new_index = int(math.fmod(new_index, 4))
    return directions[new_index]

def read_map(file_name):
    """
    Reads a map from the specified file and interprets the directions
    and steps for navigation. The map file contains information about
    the starting coordinates and the steps to be taken in a specified
    direction. The initial direction is assumed to be North.

    The map file should be structured in such a way that it lists the
    starting coordinates (x, y) followed by directions (N, E, S, W)
    and the corresponding number of steps to take in each direction.

    Note: The file may contain empty lines, which should be ignored.

    Args:
    file_name (str): The pathname of the file containing the map data.

    Returns:
    tuple: A tuple containing two elements:
        - The first element is a tuple (x, y) representing the starting
          coordinates.
        - The second element is a list of tuples, where each tuple contains:
            - A direction (str): 'N' for North, 'E' for East, 'S' for South,
              or 'W' for West.
            - The number of steps (int) to take in that direction.

    >>> read_map("treasure_3.txt")
    ((0, 11), \
[('W', 5), ('W', 6), ('S', 7), ('E', 3), ('E', 4), \
('N', 5), ('E', 2), ('S', 2), ('E', 2), ('N', 4)])
    """
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        lines = content.splitlines()
        lines = [el.split(' ') for el in lines if el != '']
        direction = 'N'
        directions = []
        for el in lines[1:]:
            direction = define_direction(direction, int(el[0]))
            directions.append((direction, int(el[1])))
        position = (int(lines[0][0]), int(lines[0][1]))
        return (position,directions)


def find_path(start, treasure_directions):
    """
    Calculates the path of coordinates based on the given start position
    and a series of directional steps. The start position is provided as
    a tuple of coordinates (x, y).

    The function interprets movement based on the following directional
    rules, with steps determining how far to move in a given direction:
    - 'W' (West): decreases the y-coordinate (moves left).
    - 'E' (East): increases the y-coordinate (moves right).
    - 'N' (North): decreases the x-coordinate (moves up).
    - 'S' (South): increases the x-coordinate (moves down).

    Args:
    start (tuple): A tuple representing the starting coordinates (x, y).
    treasure_directions (list of tuple): A list of tuples where each tuple
                                         contains:
                                         - A direction ('N', 'E', 'W', 'S')
                                         - An integer representing the number
                                           of steps to take in that direction.

    Returns:
    list of tuple: A list of coordinates (x, y) representing the path taken 
                   from the start position, including all intermediate steps.

    >>> start = (0, 0)
    >>> path = [('E', 3), ('S', 3), ('W', 3), ('N', 3)]
    >>> find_path(start, path)
    [(0, 0), \
(0, 1), (0, 2), (0, 3), \
(1, 3), (2, 3), (3, 3), \
(3, 2), (3, 1), (3, 0), \
(2, 0), (1, 0), (0, 0)\
]
    """
    the_map = [start]
    for el in treasure_directions:
        position = the_map[-1]
        x , y = position[0], position[1]
        match el[0]:
            case 'N':
                for _ in range(el[1]):
                    x -= 1
                    the_map.append((x,y))
            case 'S':
                for _ in range(el[1]):
                    x += 1
                    the_map.append((x,y))
            case 'E':
                for _ in range(el[1]):
                    y += 1
                    the_map.append((x,y))
            case 'W':
                for _ in range(el[1]):
                    y -= 1
                    the_map.append((x,y))
    return the_map


def find_treasure(path1, path2):
    """
    Determines the location of the treasure based on the intersection of
    two paths. The function identifies the point of intersection and
    calculates the treasure's location based on the following conditions:

    - If the paths intersect at exactly one point, that point is the
      treasure's location.
    - If the paths intersect at exactly two points, the treasure is located
      at the midpoint between these two points. If the coordinates of the
      midpoint are fractional, they are rounded down to the nearest integer.
    - If the paths intersect at more than two points, it is impossible
      to determine the treasure's exact location, and the function
      returns `None`.

    Args:
    path1 (list of tuple): The first path, represented as
                           a list of coordinates (x, y).
    path2 (list of tuple): The second path, represented as
                           a list of coordinates (x, y).

    Returns:
    tuple or None: The coordinates (x, y) of the treasure if it
    can be determined, or `None`  if the treasure's location
    cannot be identified.

    >>> path1 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0)]
    >>> path2 = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> path3 = [(1, 4), (1, 3), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4)]
    >>> find_treasure(path1, path2)
    (2, 2)
    >>> find_treasure(path1, path3)
    (1, 2)
    >>> find_treasure(path2, path3)
    """
    intersections = []
    for el in path1:
        if el in path2:
            intersections.append(el)

    if len(intersections) == 1:
        return intersections[0]
    if len(intersections) == 2:
        el1, el2 = intersections[0], intersections[1]
        x = (el1[0] + el2[0])//2
        y = (el1[1] + el2[1])//2
        return (x,y)
    return None


def find_size(path):
    """
    Calculates the size of the map based on the given path. The size of the map
    is determined by the minimal number of points needed vertically and
    horizontally to encompass the entire path. The height is the difference
    between the maximum and minimum x-coordinates, and the width is the
    difference between the maximum and minimum y-coordinates.

    Args:
    path (list of tuple): A list of coordinates (x, y) representing the path.

    Returns:
    tuple: A tuple (height, width) where:
        - height is the number of points needed vertically.
        - width is the number of points needed horizontally.

    >>> path = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> find_size(path)
    (3, 3)
    """
    horizontal = [el[0] for el in path]
    vertical = [el[1] for el in path]
    width = max(horizontal) - min(horizontal) + 1
    heigth = max(vertical) - min(vertical) + 1
    return((width,heigth))


def shift_path(path):
    """
    Shifts the given path to ensure that all coordinates are non-negative
    and the smallest coordinate is positioned at (0, 0).

    The function returns a tuple, where the first element is a tuple
    containing the minimum y and x values before the shift, and the second
    element is the list of shifted coordinates.

    Args:
    path (list of tuple): A list of tuples where each tuple represents a
                          coordinate (x, y) along the path.

    Returns:
    tuple: A tuple where:
        - The first element is a tuple representing the minimum
          y-coordinate and x-coordinate found in the path.
        - The second element is a list of tuples representing the shifted path,
          where all coordinates are non-negative.

    >>> path = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> shift_path(path)
    ((2, 2), [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2)])
    """
    init_min = min(path)
    horizontal = [el[0] for el in path]
    vertical = [el[1] for el in path]
    coeff_x = min(horizontal)
    coeff_y = min(vertical)
    new_path = []
    if coeff_x != 0:
        coeff_x = 0 - coeff_x
    if coeff_y != 0:
        coeff_y = 0 - coeff_y
    for el in path:
        x, y = el[0] + coeff_x, el[1] + coeff_y
        new_path.append((x, y))
    return (init_min, new_path)


def decode_map(file_name1, file_name2, map_file_name):
    """
    Draws a map that visualizes two paths and the treasure (if it exists)
    based on the paths provided in two input files. The map is written
    to the specified output file.

    - The paths are marked with `.`.
    - The start of the first path is marked with `1`.
    - The start of the second path is marked with `2`.
    - If the start of the first and second path coincides, it is
      marked with `3`.
    - If the treasure is found (i.e., the paths intersect at a specific point),
      it is marked with `x`. The treasure marker `x` overwrites the start
      markers '1' and '2' if they coincide with the treasure's location.

    Args:
    file_name1 (str): The name of the file containing the first path.
    file_name2 (str): The name of the file containing the second path.
    map_file_name (str): The name of the output file where the map will be drawn.

    Returns:
    None: The map is written directly to the output file.

    >>> decode_map('treasure_1.txt', 'treasure_2.txt', 'output.txt')
    >>> with open('output.txt', 'r', encoding='utf-8') as file:
    ...    print(file.read())
    1..  
    . .  
    ..x.2
      . .
      ...
    """
    map1 = read_map(file_name1)
    map2 = read_map(file_name2)
    path1 = find_path(map1[0], map1[1])
    size1 = find_size(path1)
    path1 = shift_path(path1)[1]
    path2 = find_path(map2[0],map2[1])
    size2 = find_size(path2)
    result, new_line = '', '\n'
    final_map = [[ " " for _ in range(size1[0]+size2[0])] for _ in range(size1[1]+size2[1]-1)]
    for el in path1:
        x, y = el[0], el[1]
        if x == 0 and y == 0:
            final_map[x][y] = "1"
        else:
            final_map[x][y] = "."
    start_path2 = list(map2[0])
    for el in path2:
        x, y = el[0], el[1]
        if x == start_path2[0] and y == start_path2[1]:
            final_map[x][y] = "2"
        else:
            final_map[x][y] = "."
    intersection = list(find_treasure(path1, path2))
    x,y = intersection
    final_map[x][y] = "x"
    for i, row in enumerate(final_map):
        row = [str(el) for el in row]
        line = ''.join(row)
        line = line.rstrip()
        if i == len(final_map) - 1:
            new_line = ''
        result += line + new_line
    with open(map_file_name, "w", encoding="utf-8") as file:
        file.write(result)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
