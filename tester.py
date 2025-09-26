from main import MyAI
import random

def add_random_move():
    rand_x = random.randint(0, 3)
    rand_y = random.randint(0, 3)
    return (rand_x, rand_y)

def add_move(move, board, who):
    board = [[[board[x][y][z] for z in range(4)] for y in range(4)] for x in range(4)]
    for z in range(4):
        if board[z][move[0]][move[1]] == 0:
            board[z][move[0]][move[1]] = who
            return board
# TEST
def main():
    # Create a 4x4x4 cube filled with 0
    board = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    ai = MyAI()

    for i in range(10):
        # if ai.is_terminal(board):
        #     print("Game Over")
        #     break
        random = add_random_move()
        board = add_move(random, board, 2)
        # if ai.is_terminal(board):
        #     print("Game Over2")
        #     break
        result = ai.get_move(board, 1, [0, 0])
        
        print(f"enemy: {random}  AI : {result}")  # Expected output:
        board = add_move(result, board, 1)
        
    
    print("New board after AI move:", board)


    for z in range(4):
        print(f"Layer {z}:")
        for y in range(4):
            print(board[z][y])
        print()

    # print("Board state: ", board)
if __name__ == "__main__":
    main()