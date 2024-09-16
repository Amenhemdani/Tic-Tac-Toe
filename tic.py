

class TicTacToe():


    def __init__(self):
        self.board=[[" " for _ in range(3)] for _ in range(3)]
        self.i=0

    def current_player(self,i):
        self.i=i
        ind=["x","o"]
        return ind[i]

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
        return False
            

    def print_board(self):
        board=self.board
        for i in range(3):
            for j in range(3):
                print(board[i][j] , end=' ')
            print()

    def switch_player(self):
        board=self.board
        lst=[i for l in board for i in l if i==" "]
        print(len(lst))
        if len(lst)%2==0:
            i=1
        else:
            i=0
        x=self.current_player(i)
        return x
        

    def make_move(self,row, col):
        board=self.board
        if board[row][col]==" ":
            x=current_player(self.i)
            board[row][col]==x
            lst=[i for l in board for i in l if i==" "]
            if len(lst)<=4:
                self.check_winner(board)
            elif len(lst)==0:
                self.check_draw() if self.check_winner(board)==False else self.check_winner(board) 

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
        board=self.board


game=TicTacToe()
game.print_board()


game.play()
