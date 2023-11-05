from node import Node



def astar(start_point, goal_point, map):
    """
    Find the path from the start point to the goal point using the A* algorithm.

    Args:
        start_point (tuple[int, int]): The starting point on the map.
        goal_point (tuple[int, int]): The goal point on the map.
        map (list[list[int]]): The map representing the grid where 'x' represents obstacles.

    Returns:
        list[tuple[int, int]]: A list of coordinates representing the path from the start to the goal, or None if no path is found.
    """
    # Create start and end node
    start_node = Node(start_point)
    end_node = Node(goal_point)

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        # TODO: Optimize this - use a heap.
        current_node = min(open_list)  # type: Node

        # Pop current off open list, add to closed list
        open_list.remove(current_node)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            while current_node != start_node:
                path.append(current_node.point)
                current_node = current_node.parent
            path.append(start_node.point)
            path.reverse()
            return path

        # Get children points
        adjacent_points = current_node.get_adjacent_points(map)

        # Loop through children
        for adjacent_point in adjacent_points:
            adjacent_node = Node(adjacent_point)
            adjacent_node.parent = current_node

            if adjacent_node in closed_list:
                continue
            if map[adjacent_point[0]][adjacent_point[1]] == 'x':
                continue

            adjacent_node.g = current_node.g + int(
                map[adjacent_point[0]][adjacent_point[1]]
            )
            # adjacent_node.g = current_node.g + 1

            adjacent_node.h = adjacent_node.h_cost(goal_point)
            adjacent_node.f = adjacent_node.g + adjacent_node.h

            if adjacent_node in open_list:
                if adjacent_node.g > current_node.g:
                    continue
            open_list.append(adjacent_node)
    return None
