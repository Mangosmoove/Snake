import queue

#https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
#Took inspiration from this BFS algorithm, code is not exact but conceptually similar
#Although BFS will be similar usually no matter what.

def bfs(size_x, size_y, block_size, visited, goal, start):
    #https://www.tutorialspoint.com/stack-and-queue-in-python-using-queue-module
    Q = queue.Queue(maxsize = 0)
    Q.put(start)
    graph = {}
    
    try:
        while Q.empty() == False:
            #Use .get() maybe helps error
            cell = Q.get()

            if cell in visited:
                pass

            elif cell == goal:
                break

            else:
                nextCell = [cell[0] + block_size, cell[1]]
                previousCell = [cell[0] - block_size, cell[1]]
                nextnextCell = [cell[0], cell[1] + block_size]
                prevprevCell = [cell[0], cell[1] - block_size]

                searching = [nextCell, previousCell, nextnextCell, prevprevCell]
                visited.append(cell)

                for i in searching:
                    if i[0] >= size_x \
                            or i[1] >= size_y \
                            or i[0] < 0\
                            or i[1] < 0 \
                            or i in visited:

                        pass

                    else:
                        convert = str(i)
                        graph[convert] = cell
                        Q.put(i)

        return getPath(graph, start, goal)

    except KeyError:
        print("Snake Died")

def getPath(graph, start, end):
    path = [end]

    while path[-1] != start:
        path.append(graph[str(path[-1])])

    path.reverse()
    return path
