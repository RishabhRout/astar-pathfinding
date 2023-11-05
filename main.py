from astar import astar

map = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start_point = (0, 0)
goal_point = (4, 4)

if __name__ == '__main__':
    print('Map:')
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in map]))
    path = astar(start_point, goal_point, map)

    final_map = map.copy()

    if path:
        for point in path:
            final_map[point[0]][point[1]] = '+'
    else:
        print('Path not found')

    print('Path:')
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in final_map]))
