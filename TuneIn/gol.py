"""
Game of Life (TuneIn Assessment)

A cell is represented by an (x, y) pair.
The world at a given tick is a set of live cells.

"""


# map number of neighbors to whether a cell lives (index = number of neighbors)
STAYS_ALIVE = [False, False, True, True, False, False, False, False, False]
DEAD_ARISES = [False, False, False, True, False, False, False, False, False]

GLIDER = [(0, 1), (1, 0), (-1, -1), (0, -1), (1, -1)]

OUTPUT_WIDTH = 25
OUTPUT_DEPTH = 25
OUTPUT_START_X = -12
OUTPUT_START_Y = 12

def neighbors((i, j)):
    return [(x, y) for x in range(i-1, i+2)
                   for y in range(j-1, j+2) if x != i or y != j]


def neighbor_count(cell, world):
    return sum([1 for n in neighbors(cell) if n in world], 0)


def transition_the_living(world):
    """ Determine which of the living make it to the next world

        input: set of living cells
    """

    return set([ c for c in world if STAYS_ALIVE[neighbor_count(c, world)] ])


def raise_the_dead(world):
    """ go through the neigbors of the living to see which dead ones should live

        NOTE:  A dead cell coming to life must have a live eighbor (3 actually),
               so, the only candidates are the dead neighbors of the living

        input: set = [ (i, j) for each living cell ]
    """

    candidates = set([n for cell in world for n in neighbors(cell) if n not in world])
    return set([ n for n in candidates if DEAD_ARISES[neighbor_count(n, world)] ])


def next_world(thisWorld):
    """ return the next world given th ecurrent one """

    return transition_the_living(thisWorld) | raise_the_dead(thisWorld)


def output_world(world):

    print world

    replace = lambda l, n, x:  l[:n] + x + l[n+1:] if n >=0 and n < len(l) else l

    grid = [' ' * OUTPUT_WIDTH] * OUTPUT_DEPTH
    for (i, j) in world:
        x = i - OUTPUT_START_X
        y = j + OUTPUT_START_Y # y axis is upside down in the grid
        if (y >= 0 and y < OUTPUT_DEPTH):
            grid[y] = replace(grid[y], x, 'X')

    print '|' + ('-' * OUTPUT_WIDTH) + '|'
    for i in range(len(grid))[-1::-1]:
        print '|' + grid[i] + '|', i - OUTPUT_START_Y
    print '|' + ('-' * OUTPUT_WIDTH) + '|'
    print '\n'


def main():
    thisWorld = set(GLIDER)
    for i in range(100):
        if True: #i%4 == 0:
            output_world(thisWorld)
        thisWorld = next_world(thisWorld)


if __name__ == '__main__':
    main()
