# Project 02 Q01 - Armaan Bhandal

import random

def fill_board():
    cards = list(range(1, 9)) * 2
    random.shuffle(cards)
    return [cards[i:i+4] for i in range(0, 16, 4)]

def show_board(board, revealed):
    for i in range(4):
        for j in range(4):
            if revealed[i][j]:
                print(f"{board[i][j]:2}", end=" ")
            else:
                print(" *", end=" ")
        print()

def get_card_location(revealed):
    while True:
        try:
            row, col = map(int, input("Enter the row (1 to 4) and col (1 to 4) position of the pair: ").split())
            if 1 <= row <= 4 and 1 <= col <= 4:
                if not revealed[row - 1][col - 1]:
                    return row - 1, col - 1
                else:
                    print("Card at this position already faced up. Select again!")
            else:
                print("Invalid position.")
        except ValueError:
            print("Invalid input. Enter two numbers separated by a space.")

def play_game(board):
    revealed = [[False] * 4 for _ in range(4)]
    while not all(all(row) for row in revealed):
        show_board(board, revealed)

        row1, col1 = get_card_location(revealed)
        revealed[row1][col1] = True
        show_board(board, revealed)

        row2, col2 = get_card_location(revealed)
        revealed[row2][col2] = True
        show_board(board, revealed)

        if board[row1][col1] != board[row2][col2]:
            print("Pair do not match. Select again!")
            revealed[row1][col1] = revealed[row2][col2] = False
        else:
            print("Pair match!")

def main():
    board = fill_board()
    play_game(board)
    print("Congratulations! You matched all pairs.")

if __name__ == "__main__":
    main()
