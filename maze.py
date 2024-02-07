from problem import Problem
class Maze(Problem):
    def __init__(self, maze:list):
        self.width=len(maze[0])
        self.height=len(maze)
        super().__init__(initial=(0, 0), goal=(self.width-1, self.height-1))
        self.maze=maze

    def acts(self, state):
        maze=self.maze
        actlist=[]
        x=state[0]
        y=state[1]
        if x < self.width-1:
            if maze[y][x+1] == 0:
                actlist.append('right')
        if y < self.height-1:
            if maze[y+1][x] == 0:
                actlist.append('down')
        if x>0:
            if maze[y][x-1]==0:
                actlist.append('left')
        if y > 0: 
            if maze[y-1][x] == 0:
                actlist.append('up')
        return actlist
    
    def trans(self, state, act):
        x = state[0]
        y = state[1]
        if act == 'right':
            return (x+1, y)
        if act == 'down':
            return (x, y+1)
        if act == 'left':
            return (x-1,y)
        if act == 'up':
            return (x, y-1)
    
    def show(self,node):
        return node.state


if __name__ == '__main__':
    maze =[[0,1,0,0,0],
           [0,0,0,1,0],
           [1,1,1,0,0],
           [0,0,1,0,1],
           [0,0,0,0,0]]
    mazeobj = Maze(maze=maze)
    res = mazeobj.search().path()
    for state in res:
        maze[state[1]][state[0]]=2
    for line in maze:
        print(line)
