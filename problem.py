class Problem:
    def __init__(self,initial,goal=None):
        self.initial=initial
        self.goal=goal
    def acts(self,state) -> list: #return all of allow states
        raise NotImplementedError
    def trans(self,state,act) -> tuple: #return changed state
        raise NotImplementedError
    def show(self,node) -> object:  # return how to show the transform
        return node
    def test(self, state):
        return state==self.goal
    def search(self):
        frontier=[Node(self,self.initial)]
        explored=set()
        while frontier:
            node=frontier.pop(0)
            if self.test(node.state):
                return node
            explored.add(node.state)
            frontier.extend([n for n in node.expand() if n.state not in explored])
    
class Node:
    def __init__(self,problem,state,parent=None,act=None):
        self.state=state
        self.parent=parent
        self.act=act
        if problem:
            self.problem=problem
    
    def expand(self):
        childs=[]
        for act in self.problem.acts(self.state):
            state=self.problem.trans(self.state,act)
            childs.append(Node(self.problem,state,self,act))
        return childs

    def path(self,show_function=None):
        if show_function is None:
            show_function=self.problem.show
        show=show_function(self)
        if self.parent is None:
            if show is None:
                return []
            return [show]
        return self.parent.path(show_function)+[show]
    
    def __eq__(self,other):
        return isinstance(other,Node) and self.state==other.state
    
def search(problem):
    return problem.search()
    