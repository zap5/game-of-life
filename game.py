from random import randint

class Life():

    def __init__(self):
        self.board = []
    
    def random_state(self, height, width):
        self.board = [[]] * height
        
        for i in range(height):
            self.board[i] = [0] * width 

            for j in range(width):
                self.board[i][j] = randint(0, 1)
        
        return self.board

print(Life().random_state(3, 9))
