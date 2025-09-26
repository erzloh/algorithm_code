from main import MyAI
import random

def add_random_move(board):
    rand_x = random.randint(0, 3)
    rand_y = random.randint(0, 3)
    print("Random move :", (rand_y, rand_x))
    board = [[[board[x][y][z] for z in range(4)] for y in range(4)] for x in range(4)]
    for z in range(4):
        if board[z][rand_y][rand_x] == 0:
            board[z][rand_y][rand_x] = 2
            return board

# TEST
def main():
    # Create a 4x4x4 cube filled with 0

    board = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    board = add_random_move(board)
    ai = MyAI()
    result = ai.get_move(board, 1, [0, 0])

    print("AI :", result)  # Expected output:
if __name__ == "__main__":
    main()