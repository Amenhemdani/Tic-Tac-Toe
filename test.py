def check_row_col(board):
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


board=[[" " for _ in range(3)] for _ in range(3)]
def check_row(board):
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
        return -1

def check_column(board):
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
        return -1

def check_diagonal_1(board):
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

def check_diagonal_2(board):
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
