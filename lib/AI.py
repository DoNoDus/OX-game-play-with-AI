# from easyAI import AI_Player, Human_Player, Negamax, TwoPlayerGame

from lib.Player import AI_Player, Human_Player
from lib.TwoPlayGame import TwoPlayerGame
from lib.Negamax import Negamax

class GameController(TwoPlayerGame):

    def __init__(self, players, board):
        self.players = players
        self.current_player = 1
        self.board = board
        self.possible_combinations = [[1, 2, 3], [4, 5, 6],
                                      [7, 8, 9], [1, 4, 7],
                                      [2, 5, 8], [3, 6, 9],
                                      [1, 5, 9], [3, 5, 7]]
        # print('---> Do GameController Class!!')

    def possible_moves(self):
        # print('---> Do possible_moves function')
        return [a + 1 for a, b in enumerate(self.board) if b == 0]
        # return ช่องที่สามารถขยับไปได้

    def make_move(self, move):
        # print('---> Do make_move function')
        self.board[int(move) - 1] = self.current_player

    def loss_condition(self):
        # print('---> Do loss_condition')
        # possible_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        return any([all([(self.board[i - 1] == self.opponent_index) for i in combination]) for combination in  self.possible_combinations])

        # return --> all([(self.board[i - 1] == self.opponent_index) for i in combination]) คือการ check เงื่อนไขภายใน possible_combinations (ต้องถูกท้องหมด)
        #        --> any([all([(self.board[i - 1] == self.opponent_index) for i in combination]) for combination in possible_combinations]) คือการ เงื่อนไข end game (อันใดอันนึงถูก)

    def is_over(self):
        # print('---> Do is_over function')
        return (self.possible_moves() == []) or self.loss_condition()

    def show(self):
        # print('---> Do show function')
        print('\n'.join([' '.join([['.', 'O', 'X'][self.board[3 * j + i]] for i in range(3)]) for j in range(3)]))
        for count, possible_set in enumerate(self.possible_combinations):
            if all([(self.board[i-1]) == 2 for i in possible_set]) :
                print("\n -- AI Win --")
                return 'AI WIN'
            elif all([(self.board[i-1]) == 1 for i in possible_set]) :
                print("\n --- Player Win ---")
                return 'PLAYER WIN'
            else:
                if 0 not in self.board and count+1 == len(self.possible_combinations):
                    print('\n ---- Tie ----')
                    return 'TIE'

    def get_board(self):
        return self.board

    def scoring(self):
        # print('---> Do scoring function')
        return -100 if self.loss_condition() else 0

class Start_game:
    def start_game(self, board):
        algorithm = Negamax(7)
        self.new_board = GameController([Human_Player(), AI_Player(algorithm)], board).play()
        return self.new_board

if __name__ == '__main__':
    algorithm = Negamax(7)
    GameController([Human_Player(), AI_Player(algorithm)]).play()



