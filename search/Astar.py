from queue import PriorityQueue as pq
from copy import deepcopy

class State:
    def __init__(self, board, move, parent=None):
        self.board = board
        self.move = move
        self.parent = parent
        
    '''class compared magic method'''
    def __lt__(self, other):
        return 0
        
    '''Returns the position of the empty block'''
    def where_is_zero(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i,j
    
    def l1_distance(self, goal):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != goal[i][j]:
                    distance +=1
        return distance
    
    def generate_states(self):
        zero_x, zero_y = self.where_is_zero()
        board = self.board
        allstates = []
        
        if not zero_x - 1 < 0: #can be moved upwards
            board_up = deepcopy(board)
            board_up[zero_x][zero_y] = board_up[zero_x - 1][zero_y]
            board_up[zero_x - 1][zero_y] = 0 #swap
            board_up_state = State(board_up,'down',self)
            allstates.append(board_up_state)
            
        if zero_x + 1 < 3: #can be moved downwards
            board_down = deepcopy(board)
            board_down[zero_x][zero_y] = board_down[zero_x + 1][zero_y]
            board_down[zero_x + 1][zero_y] = 0
            board_down_state = State(board_down,'up',self)
            allstates.append(board_down_state)
            
        
        if not zero_y - 1 < 0: #can be moved left
            board_left = deepcopy(board)
            board_left[zero_x][zero_y] = board_left[zero_x][zero_y - 1]
            board_left[zero_x][zero_y - 1] = 0
            board_left_state = State(board_left,'right',self)
            allstates.append(board_left_state)
            
        if zero_y + 1 < 3: #can be moved right
            board_right = deepcopy(board)
            board_right[zero_x][zero_y] = board_right[zero_x][zero_y + 1]
            board_right[zero_x][zero_y + 1] = 0
            board_right_state = State(board_right,'left',self)
            allstates.append(board_right_state)
            
        return allstates
    
    ''' Stores all the parents 'traceback' of a state. '''
    def traceback(self):
        path = []
        path.append((self.move, self.board))
        n = self.parent
        while n.parent is not None:
            path.append((n.move, n.board))
            n = n.parent
        path.append((n.move, n.board))
        path.reverse()
        return path
    
'''A star function'''

#init_state = State([[2, 8, 3], [1, 6, 4], [7, 0, 5]], 'start')
#goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
init_state = State([[1,4,3],[7,0,6],[5,8,2]], 'start')
goal_state = [[1,3,6],[7,4,2],[5,8,0]]

def Astar(init_state, goal_state):
    PQueue = pq()
    visited = []
    explored = 0
    PQueue.put((init_state.l1_distance(goal_state), init_state))
    
    while not PQueue.empty():
        h, n = PQueue.get() #heuristic and node
        
        if n.board in visited:
            continue
            
        if h==0: # Gameset
            print('Gameset!')
            print(f'Explored states {explored}')
            draw_path(n.traceback())
            return
        
        visited.append(n.board)
        explored += 1
        
        for nstate in n.generate_states():
            PQueue.put((nstate.l1_distance(goal_state), nstate))
            
def draw_board(board):
    print(f'___________')
    for i in board:
        print('|%d|%d|%d| '%(i[0],i[1],i[2]))
        print('___________ ') 

def draw_path(path):
    for b in path:
        print('')
        print(f'{b[0]}, (h = {State(b[1],b[0]).l1_distance(goal_state)})')
        draw_board(b[1])
    print('END') 


Astar(init_state, goal_state)