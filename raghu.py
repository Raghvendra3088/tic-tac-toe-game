def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    # Check for tie
    if all(cell != ' ' for row in board for cell in row):
        return 'Tie'
    
    return None

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    break
                print("Invalid move. Try again.")
            except ValueError:
                print("Please enter numbers between 0 and 2.")
        
        board[row][col] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"Player {winner} wins!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    while True:
        play_game()
        if input("Play again? (y/n): ").lower() != 'y':
            break
    print("Thanks for playing!")
