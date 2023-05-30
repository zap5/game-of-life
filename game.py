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
        living_neighbor_count = 0
        current_row_index = x 
        row_above_index = current_row_index - 1
        row_below_index = current_row_index + 1

        cell_index = y
        right_cell_index = y + 1
        left_cell_index = y - 1

        try:
            for i in range(row_above_index, row_below_index):
                for j in range(left_cell_index, right_cell_index):
                    if self.board[i][j] == 1:
                        living_neighbor_count += 1
        except IndexError:
            pass
        return living_neighbor_count
    
    def next_board_state(self):
        # Any cell with 0 to 1 live neighbors becomes dead, because of underpopulation
        # Any cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
        # Any cell with more than 3 live neighbors dies, due to overpopulation
        # Any dead cell with exactly 3 neighbors becomes alive, due to reproduction

        new_board = self.board
        
        for i in range(self.height):
            for j in range(self.width):
                live_ones = self.check_neighbors(i, j)
                if live_ones <= 1:
                    new_board[i][j] = 0
                elif live_ones == 2:
                    pass
                elif live_ones == 3: 
                    new_board[i][j] = 1
                elif live_ones > 3:
                    new_board[i][j] = 0
        
        self.board = new_board


x = Life()
x.set_board_size(10, 20)
x.random_state()

while True:
    x.render_board()
    x.next_board_state()
    sleep(1)