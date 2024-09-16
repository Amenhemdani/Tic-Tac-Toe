

class TicTacToe():

    def __init__(self):
        self.board=[[" " for _ in range(3)] for _ in range(3)]
        self.i=0
        self.lst=[item for l in self.board for item in l if item==" "]

    def choice(self):
        row=input("Enter the index of row")
        while row not in ["0","1","2"]:
            row=input("Enter the index of row")
        col=input("Enter the index of column")
        while col not in ["0","1","2"]:
            col=input("Enter the index of column")
        self.make_move(int(row), int(col))
        
    def current_player(self):
        ind=["x","o"]
        return ind[self.i]

    def check_row_col(self,board):
        occur={
        "row":board[0][0],
        "col":board[0][0],
        "diag1":board[0][0],
        "diag2":board[0][2]
        }
        for i in range(1,3):
            occur["row"]+=board[0][i]
            occur["col"]+=board[i][0]
            occur["diag1"]+=board[i][i]
            occur["diag2"]+=board[2-i][2-i]
        for value in occur.values():
            x=value.count("x")
            o=value.count("o")
            if x==3:
                return 0
            elif o==3:
                return 1
        return -1
            
    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j] , end=' ')
            print()

    def switch_player(self):
        lst=[item for l in self.board for item in l if item==" "]
        if len(lst)%2==0:
            self.i=1
        else:
            self.i=0
        x=self.current_player()
        return x
        
    def make_move(self,row, col):
        if self.board[row][col]==" ":
            x=self.switch_player()
            self.board[row][col]=x
            lst=[item for l in self.board for item in l if item==" "]
            if len(lst)<=4:
                self.check_winner(self.board)                
            elif len(lst)==0:
                self.check_draw() if self.check_winner(self.board)==False else self.check_winner(self.board) 

        else:
            print("This is already occupied , Try again")
            self.choice()

    def check_winner(self,board):
        players=["Player 1","Player 2"] 
        win=self.check_row_col(board)
        if win in [0,1]:
            print(f"The {players[win]} is winning") 
        else:
            return False
   
    def check_draw(self):
        print("\nDraw")

    def play(self):
        lst=[item for l in self.board for item in l if item==" "]
        self.print_board()
        while len(lst)!=0 and self.check_winner(self.board) is False:
            self.choice()
            self.print_board()
            self.switch_player()
        print("Game over")

game=TicTacToe()

game.play()
