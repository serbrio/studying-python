def stone_wall(wall):
    """
    Input: a multiline string consists of '0' and '#' - a view of a stone wall from above.
    The '#' will show the stone part of the wall and the '0' will show the empty part.
    The relative location of you and the wall is as follows:
    you look at the array from the bottom of it.
    Your task is to find the index of the place where the wall is the narrowest:
    the max number of '0' in column.
    The width of the wall is the height of the columns of the array (multiline string).
    If there are several such places, return the index of leftmost. Index starts from 0.
    """
    wall_lines = wall.split()
    wall_lines.reverse()  # to 'look' at the wall from bottom
    wholes = {x: 0 for x, y in enumerate(wall_lines[0])}
    for column in range(len(wall_lines[0])):
        for line in wall_lines:
            if line[column] == "0":
                wholes[column] += 1
    maxpair = max(sorted(wholes.items()), key=lambda x: x[1])
    return maxpair[0]

if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##########
####0##0##
00##0###00
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")