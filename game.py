from random import random
from time import sleep

class Life():

    def __init__(self):
        self.board = []
        self.height = 0
        self.width = 0

    def set_board_size(self, height, width):
        self.height = height
        self.width = width

        self.board = [[]] * self.height

        for i in range(self.height):
            self.board[i] = [0] * self.width 
    
    def random_state(self):
        
        for i in range(self.height): 
            for j in range(self.width):
                random_number = random()
                cell_state = 0

                if random_number > 0.7:
                    cell_state = 1

                self.board[i][j] = cell_state
        
        return self.board
    
    def print_border(self):
        border = '-' * self.width
        print(border)
    
    def render_board(self):
        self.print_border()

        for i in range(self.height):
            line = ''
            for j in range(self.width):
                cell = '_'
                
                if self.board[i][j] == 1:
                    cell = '8'
                
                line = line + cell
            print(line)
        
        self.print_border()
    
    def check_neighbors(self, x, y):
        # Takes a given cell and counts how many of its neighbors are alive

        living_neighbor_count = 0
        row_index = x 

        cell_index = y

        for i in range(row_index - 1, row_index + 2):
            if i < 0 or i >= self.height:
                continue
            # print("Checking row ", str(i))
            for j in range(cell_index - 1, cell_index + 2):
                if j < 0 or j >= self.width:
                    continue
                if i == x and j == y:
                    continue
                # print("Checking neighbors in row ", str(i),  ", cell ", str(j))
                if self.board[i][j] == 1:
                    living_neighbor_count += 1
                    # print("Living neighbor count is now ", str(living_neighbor_count))
        return living_neighbor_count
    
    def copy_board(self):
        # Creates a new 2D list to store board state, because if you just try to assign board state to a variable and 
        # then make changes to that variable it also overwrites board state.

        new_board = [[]] * self.height
        for i in range(self.height):
            new_board[i] = [0] * self.width 

        for i in range(self.height):
            for j in range(self.width):
                new_board[i][j] = self.board[i][j]
        
        return new_board

    def determine_next_board_state(self):
        # Any cell with 0 to 1 live neighbors becomes dead, because of underpopulation
        # Any cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
        # Any cell with more than 3 live neighbors dies, due to overpopulation
        # Any dead cell with exactly 3 neighbors becomes alive, due to reproduction
        
        new_state_board = self.copy_board()
        # Write all changes safely to a copy so that we do not overwrite board state during the checking process
        
        for i in range(self.height):
            for j in range(self.width):
                # print("Checking neighbors of cell ", str(i), ", ", str(j))
                live_ones = self.check_neighbors(i, j)
                # print("Live ones count: ", str(live_ones))
                # print("Value of cell ", str(i), ", ", str(j), ": ", str(self.board[i][j]))
                if live_ones <= 1:
                    new_state_board[i][j] = 0
                elif live_ones == 2:
                    continue
                elif live_ones == 3: 
                    new_state_board[i][j] = 1
                elif live_ones > 3:
                    new_state_board[i][j] = 0
                
                # print("Value of cell ", str(i), ", ", str(j), ": ", str(self.board[i][j]))
        
        return new_state_board
    
    def set_next_board_state(self):
        next_board_state = self.determine_next_board_state()

        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j] = next_board_state[i][j]


x = Life()
x.set_board_size(50, 200)
x.random_state()
# x.board = [[1, 0, 1], [0, 0, 0], [1, 0, 0]]

while True:
    x.set_next_board_state()
    x.render_board()
    sleep(1)