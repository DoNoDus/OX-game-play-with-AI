import tkinter as tk
from lib.AI import *
from lib.TwoPlayGame import *

class TkInterface:
    def __init__(self):
        global root
        root = tk.Tk()
        root.title("XO Games")
        root.iconbitmap(r'images/xo.ico')
        self.tk_start()
        root.mainloop()
        
    def tk_start(self):

        for widget in root.winfo_children():
            widget.destroy()

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 690
        window_height = 840
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
        self.O_image = tk.PhotoImage(file='images/o.png')
        self.X_image = tk.PhotoImage(file='images/x.png')
        def row_col(key):
            if key >= 0 and key < 3:
                return 0, key
            elif key >= 3 and key < 6:
                return 1, key - 3
            else:
                return 2, key - 6

        for key in key_O:
            row, col = row_col(key)
            label = tk.Label(image=self.O_image)
            label.grid(row=row, column=col)
            self.board_button[key].config(text='0', background='#DBFFAE', borderwidth=0, command=lambda :self.not_move())

        for key in key_X:
            row, col = row_col(key)
            label = tk.Label(image=self.X_image)
            label.grid(row=row,column=col)
            self.board_button[key].config(text='X', background='#FF8E76', borderwidth=0, command=lambda :self.not_move())

        if self.status in ['AI WIN', 'PLAYER WIN', 'TIE']:
            # for i in range(len(self.board)):
            #     self.board_button[i].destroy()
            if self.status == 'AI WIN':
                self.status_img = tk.PhotoImage(file='images/1.png')
            elif self.status == 'PLAYER WIN' :
                self.status_img = tk.PhotoImage(file='images/2.png')
            else:
                self.status_img = tk.PhotoImage(file='images/3.png')

            self.label = tk.Label(root, image=self.status_img)
            self.label.grid(row=3,column=1)
            self.restart_image = tk.PhotoImage(file='images/RESTART.png')
            self.restart_button = tk.Button(root, image=self.restart_image, borderwidth=0, command=lambda :self.tk_start())
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
