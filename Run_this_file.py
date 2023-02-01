import tkinter as tk
from AI import *
from TwoPlayGame import *

class TkInterface:
    def __init__(self):
        global root
        root = tk.Tk()
        root.title("3x3 Grid of Buttons")
        self.tk_start()
        root.mainloop()

    def tk_start(self):

        for widget in root.winfo_children():
            widget.destroy()

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 750
        window_height = 850
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate - 100))

        self.board = [0] * 9

        i = 1
        self.board_button = []
        for row in range(3):
            for col in range(3):
                self.board_button.append(tk.Button(root, text=str(i), font=15, height=10, width=20,
                                                   command=lambda i=i: self.tk_make_move(i)))
                self.board_button[-1].grid(row=row, column=col)
                i += 1

    def board_config(self):
        key_O = [key for key, val in enumerate(self.board) if val == 1]
        key_X = [key for key, val in enumerate(self.board) if val == 2]
        print("key_O", key_O)
        print("key_X", key_X)
        for key in key_O:
            self.board_button[key].config(text='O', background='#54FE85', command=lambda :self.not_move())
        for key in key_X:
            self.board_button[key].config(text='X', background='#FF8E76', command=lambda :self.not_move())

        if self.status in ['AI WIN', 'PLAYER WIN', 'TIE']:
            # for i in range(len(self.board)):
            #     self.board_button[i].destroy()
            self.label = tk.Label(root, text=self.status, font=20)
            self.label.grid(row=3,column=1)
            self.restart_button = tk.Button(root, text='RESTART ?',font=20, command=lambda :self.tk_start())
            self.restart_button.grid(row=4, column=1)

    def not_move(self):
        pass

    def tk_make_move(self, move):
        TwoPlayerGame.move_response = str(move)
        self.status = Start_game.start_game(Start_game, self.board)
        self.board_config()
        print('self.board =', self.board)
        print('self.status =', self.status)


if __name__ == '__main__':
    TkInterface()
