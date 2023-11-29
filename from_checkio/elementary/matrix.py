"""
As the input data you will get the multiline string
which consists of '0' & '#'.
where '0' means the empty piece of the ground
and the '#' is the piece of your house.
Your task is to count the minimal area of the rectangle ground
which is enough for the building.
"""


def house(plan):
    if '#' not in plan:
        return 0
    grid = plan.split()
    no_so, east, west = [], [], []
    for index, line in enumerate(grid):
        if '#' in line:
            no_so.append(index)
            east.append(line.find('#'))
            west.append(line.rfind('#'))
    return (max(no_so) - min(no_so) + 1) * (max(west) - min(east) + 1)


######################################
def house_alt(p, e=enumerate):
    t = [(x, y.rfind('#'), y.find('#')) for x, y in e(p.split()) if '#' in y]
    a, b, c = zip(*t) if t else [[0], [0], [1]]
    return (max(a)-min(a)+1)*(max(b)-min(c)+1)
######################################
