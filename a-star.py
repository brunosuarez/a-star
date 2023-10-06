import heapq
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def euclidean_distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def is_valid(self, maze):
        return (
            0 <= self.x < len(maze)
            and 0 <= self.y < len(maze[0])
            and maze[self.x][self.y] == 0
        )

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __lt__(self, other):
        return False

    def __str__(self):
        return f"({self.x}, {self.y})"


def a_star(maze, start, end):
    def heuristic(point1, point2, heuristic_type="euclidean"):
        if heuristic_type == "euclidean":
            return point1.euclidean_distance(point2)
        elif heuristic_type == "manhattan":
            return point1.manhattan_distance(point2)
        else:
            raise ValueError("Heuristic type not recognized.")

    open_set = []
    closed_set = set()

    start_point = Point(start[0], start[1])
    end_point = Point(end[0], end[1])

    start_cell = Point(start[0], start[1])
    start_cell.h = heuristic(start_point, end_point)
    heapq.heappush(open_set, (start_cell.h, start_cell))

    came_from = {}

    g_score = {start_cell: 0}
    f_score = {start_cell: start_cell.h}

    while open_set:
        _, current_cell = heapq.heappop(open_set)

        if current_cell == end_point:
            path = []
            while current_cell in came_from:
                path.append(current_cell)
                current_cell = came_from[current_cell]
            return path[::-1]

        closed_set.add(current_cell)

        for neighbor_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = current_cell + Point(neighbor_offset[0], neighbor_offset[1])

            if not neighbor.is_valid(maze) or neighbor in closed_set:
                continue

            tentative_g_score = g_score[current_cell] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_cell
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end_point)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None


if __name__ == "__main__":
    #0 caminho livre e 1 obstáculo.
    maze = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    start = (0, 0)  #Início
    end = (4, 5)    #Fim

    path = a_star(maze, start, end)

    if path:
        print("LEGENDA: ")
        print("S: Inicio / E: Fim / o: Caminho / #: Obstaculo / .: Espaco Vazio")
        print("Caminho encontrado:")
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if (row, col) == start:
                    print("S", end=" ")  #Ponto de início
                elif (row, col) == end:
                    print("E", end=" ")  #Ponto de fim
                elif Point(row, col) in path:
                    print("o", end=" ")  #Caminho
                elif maze[row][col] == 1:
                    print("#", end=" ")  #Obstáculo
                else:
                    print(".", end=" ")  #Espaço vazio
            print()
    else:
        print("Nao foi possivel encontrar um caminho.")
