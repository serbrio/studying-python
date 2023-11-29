def navigation(seaside):
    """
    Counts the sum of steps required to pick up all 3 items:
    'C', 'M', 'S' from the starting position 'Y'.
    So the result will be the sum of distance from Y to C,
    from Y to M and from Y to S.
    Note that you can walk in 8 directions:
    left, right, up, down and sideways (on the diagonal in any direction).
    Array with the objects placements.
    """
    y = [0, 0]
    c = [0, 0]
    m = [0, 0]
    s = [0, 0]

    for i in range(len(seaside)):
        for j in range(len(seaside[i])):
            if seaside[i][j] == 'Y':
                y = [i, j]
            elif seaside[i][j] == 'C':
                c = [i, j]
            elif seaside[i][j] == 'M':
                m = [i, j]
            elif seaside[i][j] == 'S':
                s = [i, j]
    y_c = max(abs(y[0] - c[0]), abs(y[1] - c[1]))
    y_m = max(abs(y[0] - m[0]), abs(y[1] - m[1]))
    y_s = max(abs(y[0] - s[0]), abs(y[1] - s[1]))

    return sum([y_c, y_m, y_s])


########################################
def navigation_alt(seaside):
    positions = {cell: (i, j) for i, row in enumerate(seaside) for j, cell in enumerate(row) if cell}
    x0, y0 = positions.pop('Y')
    return sum(max(abs(x0 - x1), abs(y0 - y1)) for x1, y1 in positions.values())
#########################################


if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [ 0,  0, 0, 0,  0],
                      [ 0,  0, 0, 0,  0],
                      ['M', 0, 0, 0, 'S']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9

    assert navigation([[0, 0, 0, 0],
                       [0, 0, 0, 'Y'],
                       [0, 0, 0, 'S'],
                       [0, 0, 0, 'C'],
                       [0, 0, 0, 'M'],
                       [0, 0, 0, 0]]) == 6
    print("Coding complete? Click 'Check' to earn cool rewards!")
