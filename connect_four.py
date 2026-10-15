PLAYER1 = "\033[31mO\033[0m"
PLAYER2 = "\033[33mU\033[0m"

BOARD = [[ '[ ]' for i in range(0,7) ] for i in range(0,6)]

def check_four():
    for row in range(0, len(BOARD)):
        for col in range(0, len(BOARD[0])):
            if BOARD[row][col] != '[ ]':
                if col + 3 < 7 and all(BOARD[row][col+i] == BOARD[row][col] for i in range(4)):
                    return True
                if row + 3 < 6 and all(BOARD[row+i][col] == BOARD[row][col] for i in range(4)):
                    return True
                if row + 3 < 6 and col - 3 >= 0 and all(BOARD[row+i][col-i] == BOARD[row][col] for i in range(4)):
                    return True
                if row + 3 < 6 and col + 3 < 7 and all(BOARD[row+i][col+i] == BOARD[row][col] for i in range(4)):
                    return True
    return False

def show_board():
    for col in BOARD:
        for row in col:
            print(row, end=' ')
        print('\n')

def check_input():
    while True:
        user_input = input("Enter the column number (1-7) or q for quit: ").strip()
        if user_input.lower() == 'q':
            raise SystemExit(0)
        if (user_input.isdigit() and 0 < int(user_input) < 8):
            return int(user_input) - 1
        else:
            print("This is not a number. Please try again.") 
            
def drop(col, chip):
    for row in range(len(BOARD)-1, -1, -1):
        if BOARD[row][col] == '[ ]':
            BOARD[row][col] = f'[{chip}]'
            return True
    return False

def is_full():
    for row in BOARD:
        for cell in row:
            if cell == '[ ]':
                return False
    return True

def main():
    turn = 0
    while True:
        show_board()
        chip = PLAYER1 if turn % 2 == 0 else PLAYER2
        print(f"Player {'1' if chip == PLAYER1 else '2'} ({chip})")
        col = check_input()
        if not drop(col, chip):
            print("Column is full, try another.")
            continue
        if check_four():
            show_board()
            print(f"Player {'1' if chip == PLAYER1 else '2'} wins!")
            break
        if is_full():
            show_board()
            print("It's a draw.")
            break
        turn += 1

main()