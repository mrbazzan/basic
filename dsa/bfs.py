import queue


# def maze():
#     return [
#         ['#', '#', '#', 'O', '#'],
#         ['#', ' ', ' ', ' ', '#'],
#         ['#', ' ', '#', ' ', '#'],
#         ['#', ' ', ' ', ' ', '#'],
#         ['#', 'X', '#', '#', '#']
#     ]

# def maze2():
#     return [
#         ['#', '#', '#', '#', 'O', '#'],
#         ['#', ' ', ' ', ' ', ' ', '#'],
#         ['#', ' ', '#', ' ', ' ', '#'],
#         ['#', ' ', '#', ' ', ' ', '#'],
#         ['#', ' ', '#', '#', ' ', '#'],
#         ['#', ' ', ' ', ' ', ' ', '#'],
#         ['#', '#', '#', 'X', '#', '#']]

maze = [
        ['#', '#', '#', '#', 'O', '#'],
        ['#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', 'X', '#', '#']]


def find_point(maze, point):
    for i, line in enumerate(maze):
        if point in line:
            return i, line.index(point)

    raise Exception(f"'{point}' not in maze")


def print_maze(maze, point, path=''):
    i, j = find_point(maze, point)

    for char in path[:-1]:
        if char == 'L':
            j = j - 1
        elif char == 'R':
            j = j + 1
        elif char == 'U':
            i = i - 1
        elif char == 'D':
            i = i + 1

        maze[i][j] = '+'

    print('\n'.join([' '.join(line) for line in maze]))


def resolve_path_coordinate(x, i, j):
    # print(x)
    for char in x:
        if char == 'L':
            j = j - 1
        elif char == 'R':
            j = j + 1
        elif char == 'U':
            i = i - 1
        else:
            i = i + 1
    return i, j


q = queue.Queue()
q.put('')

height = len(maze)
width = len(maze[0])

start = 'O'
i,j = find_point(maze, start)
while start != 'X':

    x = q.get()
    # print("Present: ", x)

    # check that present coordinate is not already
    # been passed through
    #     - if the last element is L, the next one shouldn't
    #     - be R and vice-versa
    #     - if the last element is U, the next one shouldn't
    #     - be D and vice-versa

    # print(i, j)
    # print(height, width)
    # sys.exit

    # LEFT
    # if x and x[len(x)-1] != 'R':
    a, b = resolve_path_coordinate(x + 'L', i, j)
    # print("a and b " + str(a) + " " + str(b))
    if b >= 0 and b <= width - 1:
        if maze[a][b] != '#':
            q.put(x + 'L')

    # RIGHT
    # if x and x[len(x)-1] != 'L':
    a, b = resolve_path_coordinate(x + 'R', i, j)
    # print("a and b " + str(a) + " " + str(b))
    if b >= 0 and b <= width - 1:
        if maze[a][b] != '#':
            q.put(x + 'R')

  # DOWN
    # if x and x[len(x)-1] != 'U':
    a, b = resolve_path_coordinate(x + 'D', i, j)
    # print("a and b " + str(a) + " " + str(b))
    if a >= 0 and a <= height - 1:    
        if maze[a][b] != '#':
            q.put(x + 'D')

    # UP
    # if x and x[len(x)-1] != 'D':
    a, b = resolve_path_coordinate(x + 'U', i, j)
    # print("a and b " + str(a) + " " + str(b))
    if a >= 0 and a <= height - 1:
        if maze[a][b] != '#':
            q.put(x + 'U')

    # print(q.queue)
    # print('\n')


    first, second = resolve_path_coordinate(x, i, j)
    start = maze[first][second]


print_maze(maze, 'O', path=x)

