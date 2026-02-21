class Node:
    def __init__(self, x, y, level, path_history=None):
        self.x = x
        self.y = y
        self.level = level
        self.path_history = path_history if path_history is not None else []
	
class IDDFS:
    def __init__(self):
        self.found = False
        self.directions = [(1,0), (-1,0), (0,1), (0,-1)]
        self.winning_path = []

    def init(self):
        graph = []
        self.grid_x, self.grid_y = map(int, input().split())

        for _ in range(self.grid_x):
            row = list(map(int, input().split()))
            graph.append(row)

        sx, sy = map(int, input().split())
        gx, gy = map(int, input().split())

        self.source = Node(sx, sy, 0, [(sx, sy)])
        self.goal = Node(gx, gy, float('inf'))

        max_depth = self.grid_x + self.grid_y - 1

        for limit in range(max_depth + 1):
            if self.st_iddfs(graph, limit):
                break

        if self.found:
            print(f"Path found at depth {self.goal.level} using IDDFS")
            print(f"Traversal Order: {self.winning_path}")
        else:
            print(f"Path not found at max depth {max_depth} using IDDFS")

    def st_iddfs(self, graph, limit):
        stack = [self.source]
        visited = {(self.source.x, self.source.y): 0}

        while stack:
            u = stack.pop()

            if u.x == self.goal.x and u.y == self.goal.y:
                self.found = True
                self.goal.level = u.level
                self.winning_path = u.path_history
                return True

            if u.level < limit:
                for dx, dy in self.directions:
                    v_x = u.x + dx
                    v_y = u.y + dy
                    v_level = u.level + 1

                    if (0 <= v_x < self.grid_x and
                        0 <= v_y < self.grid_y and
                        graph[v_x][v_y] == 1):

                        if ((v_x, v_y) not in visited or
                            v_level < visited[(v_x, v_y)]):

                            visited[(v_x, v_y)] = v_level
                            new_path = u.path_history + [(v_x, v_y)]
                            child = Node(v_x, v_y, v_level, new_path)
                            stack.append(child)
        return False
if __name__ == "__main__":
    iddfs = IDDFS()
    iddfs.init()
