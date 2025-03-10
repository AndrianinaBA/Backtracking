count = 0 #the global counter

def print_grid(grid):
    """Printing the grid in a nicer way"""
    for rows in grid:
        print(rows)
def count_x_cells(grid):
    """This functions counts all the X cells that sould not be visited
    The result will add up as the constraint parameter later on
    """
    counter = 0
    for rows in grid:
        for elt in rows:
            if elt == 'X':
                counter += 1
    return counter

def is_possible(row,col,grid):
    """This functions decides whether we should visit a cell or not"""
    if row >= 0 and row <len(grid) and col  >= 0 and col < len(grid[0]) and grid[row][col] != 'X':
        return True
    return False

def maze_solver(grid):
    """
    This algorithm uses backtracking for doing an exhaustive search on the grid using all the precooked functions above
    """
    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited[0][0] = 1
    def backtrack(row,col,path):
        global count
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        if grid[row][col] == 'B' and len(path) == len(grid)*len(grid[0]) - count_x_cells(grid):
            #The base case of the recursion
            count += 1
            print("eepie")
            print(path[:])
            return
        for move in moves:
            next_row = row + move[0]
            next_col = col + move[1]
              
            if is_possible(next_row,next_col,grid) and visited[next_row][next_col] == 0: #here lies the problem
                visited[next_row][next_col] = 1
                path.append((next_row,next_col))
                backtrack(next_row,next_col,path)
                #we try the possibility
                path.pop()
                #we backtrack 
                visited[next_row][next_col] = 0
                #we undo the choice in order to try another possibility
        return
    backtrack(0,0,['A'])
    #we always start from the upper left corner from A
    return count


def count_path(path :str):
    """We enter the path as a string that we will have to convert as grid in order to use all the precooked functions."""
    rows = path.split('\n')
    grid = [list(row) for row in rows]
    print_grid(grid)
    result = maze_solver(grid)
    return result

path = 'AX..\n....\n....\n..XB'
res = count_path(path)
print(res)
