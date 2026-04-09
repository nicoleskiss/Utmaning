class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        win_conditions = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a,b,c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        return None
    
    def is_draw(self):
        return " " not in self.board

    def get_board_string(self):
        return "|".join(self.board)
    
    