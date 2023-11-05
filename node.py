class Node:
    """
    A class representing a node for the A* algorithm.

    Attributes:
        point (tuple[int, int]): The coordinates of the node.
        parent (Node): The parent node in the path.
        g (int): The cost from the start node to this node.
        h (int): The heuristic cost from this node to the goal.
        f (int): The total cost (g + h) of this node.

    Methods:
        __eq__(self, other) -> bool: Check if two nodes are equal based on their coordinates.
        __lt__(self, other) -> bool: Compare two nodes based on their total cost (f value).
        __gt__(self, other) -> bool: Compare two nodes based on their total cost (f value).
        __repr__(self) -> str: Generate a string representation of the node.
        get_adjacent_points(self, map) -> list[tuple[int, int]]: Get a list of adjacent points to this node on the map.
        h_cost(self, end_point) -> int: Calculate the heuristic cost from this node to the end point.
    """

    def __init__(self, point, parent=None):
        """
        Initialize a Node instance.

        Args:
            point (tuple[int, int]): The coordinates of the node.
            parent (Node, optional): The parent node in the path. Defaults to None.
        """
        self.point = point
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other) -> bool:
        """
        Compare this node with another based on their coordinates.

        Args:
            other (Node): The other node to compare.

        Returns:
            bool: True if the nodes have the same coordinates, False otherwise.
        """
        return self.point == other.point

    def __lt__(self, other) -> bool:
        """
        Compare this node with another based on their total cost (f value).

        Args:
            other (Node): The other node to compare.

        Returns:
            bool: True if this node has a lower total cost than the other node, False otherwise.
        """
        return self.f < other.f

    def __gt__(self, other) -> bool:
        """
        Compare this node with another based on their total cost (f value).

        Args:
            other (Node): The other node to compare.

        Returns:
            bool: True if this node has a higher total cost than the other node, False otherwise.
        """
        return self.f > other.f

    def __repr__(self) -> str:
        """
        Generate a string representation of the node.

        Returns:
            str: A string representation of the node in the format "(point, g: g_value, h: h_value, f: f_value)".
        """
        return f"({self.point}, g: {self.g}, h: {self.h}, f: {self.f})"

    def get_adjacent_points(self, map) -> list[tuple[int, int]]:
        """
        Get a list of adjacent points to this node on the map.

        Args:
            map (list[list[int]]): The map representing the grid.

        Returns:
            list[tuple[int, int]]: A list of tuples representing adjacent points to this node.
        """
        adjacent_points = []
        if self.point[0] - 1 >= 0:
            adjacent_points.append((self.point[0] - 1, self.point[1]))
        if self.point[0] + 1 < len(map):
            adjacent_points.append((self.point[0] + 1, self.point[1]))
        if self.point[1] - 1 >= 0:
            adjacent_points.append((self.point[0], self.point[1] - 1))
        if self.point[1] + 1 < len(map[0]):
            adjacent_points.append((self.point[0], self.point[1] + 1))
        return adjacent_points

    def h_cost(self, end_point) -> int:
        """
        Calculate the heuristic cost from this node to the end point.

        Args:
            end_point (tuple[int, int]): The coordinates of the end point.

        Returns:
            int: The heuristic cost from this node to the end point.
        """
        return abs(self.point[0] - end_point[0]) + abs(self.point[1] - end_point[1])
