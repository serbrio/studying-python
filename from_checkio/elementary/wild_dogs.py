def pair_diff(coord_a, coord_b):
    """
    Calculates the ratio (coefficient)
    of the x and y of to given coordinates (x, y), (x1, y1).
    """
    x, y = coord_a[0], coord_a[1]
    x1, y1 = coord_b[0], coord_b[1]
    try:
        ratio = (y - y1)/(x - x1)
    except:
        return None
    return ratio


def find_funcs(pairs, coords):
    """
    Finds and returns the list of funcs:
    for every pair calculates the pairdiff(),
    gathers all the coordinates from 'coords',
    which pairdiff() with one coord from the pair
    matches the pairdiff() of the pair.
    """
    funcs = []
    for pair in pairs:
        func = [*pair]
        pairdiff = pair_diff(*pair)
        for dog in coords:
            if dog not in pair and pair_diff(dog, pair[0]) == pairdiff:
                func.append(dog)
        func = sorted(func)
        if func not in funcs:
            funcs.append(func)
    return funcs


def find_largest_funcs(funcs):
    """
    Returns the largest (== with the most number of elements(coordinates) in it)
    function of the given list 'functions'.
    """
    largest_funcs = [max(funcs, key=lambda fu: len(fu))]
    for func in funcs:
        if func != largest_funcs[0] and len(func) == len(largest_funcs[0]):
            largest_funcs.append(func)
    return largest_funcs


def find_nearest_coord_for_func(func):
    """
    Finds the smallest distance from x,y = 0,0
    to the line of the given function.
    """
    a = pair_diff(func[0], func[1])
    b = func[0][1] - (a*func[0][0])
    x = -b/a
    if x == 0 and b == 0:
        return 0
    else:
        h = (x * b)/(x**2 + b**2)**0.5
        return abs(h)


def wild_dogs(coords):
    pairs = []
    for index in range(len(coords)):
        for other in coords[index+1:]:
            pairs.append((coords[index], other))
    largest = find_largest_funcs(find_funcs(pairs, coords))
    distances = []
    for func in largest:
        distances.append(find_nearest_coord_for_func(func))
    smallest_distance = min(distances)
    if isinstance(smallest_distance, int):
        return smallest_distance
    else:
        return round(smallest_distance, ndigits=2)


def wild_dogs_alt1(coords):
    from itertools import combinations
    result = []
    for (x0, y0), (x1, y1) in combinations(coords, 2):
        A, B, C = y0-y1, x1-x0, y0*(x0-x1)-x0*(y0-y1)
        distance = abs(C)/(A**2+B**2)**0.5
        result += [(distance, (1, B/A, C/A) if A else (A/B, 1, C/B))]
    distance, *_ = max(result, key=lambda x: (result.count(x), -x[0]))
    return round(distance, 2)


if __name__ == '__main__':
    print("Example:")
    print(wild_dogs([(7, 122), (8, 139), (9, 156),
                     (10, 173), (11, 190), (-100, 1)]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert wild_dogs([(1, 2), (2, 4), (3, 6), (123, 4)]) == 0
    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0
    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63
    assert wild_dogs([(7, 122), (8, 139), (9, 156), (10, 173), (11, 190), (-100, 1)]) == 0.18

    print("Coding complete? Click 'Check' to earn cool rewards!")