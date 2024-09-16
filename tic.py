class TicTacToe():

    def __init__(self):
        self.board=[[" " for _ in range(3)] for _ in range(3)]
        self.i=0

    def check_row(self,board):
        count_x=0
        count_o=0
        for row in range(3):
            for column in range(3):
                if board[row][column]=="x":
                    count_x+=1
                elif board[row][column]=="o":
                    count_o+=1
            if count_x==3:
                return 0
            elif count_o==3:
                return 1
            count_x=0
            count_o=0
        return -1

    def check_column(self,board):
        count_x=0
        count_o=0
        for column in range(3):
            for row in range(3):
                if board[row][column]=="x":
                    count_x+=1
                elif board[row][column]=="o":
                    count_o+=1
            if count_x==3:
                return 0
            elif count_o==3:
                return 1
            count_x=0
            count_o=0
        return -1

    def check_diagonal_1(self,board):
        count_x=0
        count_o=0
        for diagonal in range(3):
            if board[diagonal][diagonal]=="x":
                count_x+=1
            elif board[diagonal][diagonal]=="o":
                count_o+=1
        if count_x==3:
            return 0
        elif count_o==3:
            return 1
        return -1

    def check_diagonal_2(self,board):
        count_x=0
        count_o=0
        for diagonal in range(3):
            if board[diagonal][2-diagonal]=="x":
                count_x+=1
            elif board[diagonal][2-diagonal]=="o":
                count_o+=1
        if count_x==3:
            return 0
        elif count_o==3:
            return 1
        return -1

    def check_all(self,board):
        index=-1
        if self.check_row(board) in [0,1]:
            index=self.check_row(board)
        elif self.check_column(board) in [0,1]:
            index=self.check_column(board)
        elif self.check_diagonal_1(board) in [0,1]:
            index=self.check_diagonal_1(board)        
        elif self.check_diagonal_2(board) in [0,1]:
            index=self.check_diagonal_2(board)
        return index     

    def print_board(self):
        print(" -------------")
        for i in range(3):
            print("",end=' | ')
            for j in range(3):
                print(self.board[i][j] , end=' | ')
            print("\n -------------")

    def choice(self,empty):
        row=input("Enter the index of row")
        while row not in ["0","1","2"]:
            row=input("Enter the index of row")
        col=input("Enter the index of column")
        while col not in ["0","1","2"]:
            col=input("Enter the index of column")
        self.make_move(int(row), int(col),empty)
        
    def current_player(self):
        index=["x","o"]
        return index[self.i]
    
    def switch_player(self,empty):
        if empty%2==0:
            self.i=1
        else:
            self.i=0
        symbol=self.current_player()
        return symbol
        
    def make_move(self,row, col,empty):
        if self.board[row][col]==" ":
            symbol=self.switch_player(empty)
            self.board[row][col]=symbol
            if empty<=4:
                self.check_winner(self.board)                
            elif empty==0:
                if self.check_winner(self.board)==False :
                    self.check_draw()
                else :
                    self.check_winner(self.board) 

        else:
            print("This is already occupied , Try again")
            self.choice(empty)

    def check_winner(self,board):
        players=["Player 1","Player 2"] 
        winner=self.check_all(board)
        if winner in [0,1]:
            print(f"The {players[winner]} is winning") 
            return True
        else:
            return False
   
    def check_draw(self):
        print("\nDraw")

    def play(self):
        empty=9
        self.print_board()
        while empty>0 and self.check_winner(self.board) is False:
            self.switch_player(empty)
            self.choice(empty)
            empty-=1
            self.print_board()
        if empty==0:
            if self.check_winner(self.board) is False:
                self.check_draw()
            else:
                self.check_winner(self.board)
        print("\nGame over\n")

game=TicTacToe()

game.play()
