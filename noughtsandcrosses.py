import random
import os.path
import json
random.seed()

board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]


def draw_board(board):
    for row in range(0, 3):
        output = "-------------\n| "
        for col in range(0, 3):
            output = output + board[row][col] + " | "
        print(output)
    print("-------------")
    print("")


def welcome(board):
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print("The board layout is shown below:")
    print("")
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")
    print("")


def initialise_board(board):
    for row in range(0, 3):
        for col in range(0, 3):
            board[row][col] = " "
    return board


def get_player_move(board):
    while True:
        try:
            cell = int(input("Choose your square (1-9): "))
            if (cell >= 1) and (cell <= 9):
                row = (cell // 3)
                col = (cell % 3) - 1
                if (cell % 3) == 0:
                    row = row - 1
                if board[row][col] == " ":
                    break
            else:
                print("Please enter a valid number.")
        except:
            print("Please enter a valid number.")
    board[row][col] = "X"
    return row, col


def choose_computer_move(board):
    spaces = []
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == " ":
                spaces.append((row, col))
    try:
        row, col = random.choice(spaces)
    except IndexError:
        board[row][col] = "X"

    board[row][col] = "O"

    square = (row*3)+(col+1)
    print("The computer has chosen square", square)
    print("")
    return row, col


def check_for_win(board, mark):
    if board[0][0] == mark and board[0][1] == mark and board[0][2] == mark:
        return True
    if board[1][0] == mark and board[1][1] == mark and board[1][2] == mark:
        return True
    if board[2][0] == mark and board[2][1] == mark and board[2][2] == mark:
        return True
    if board[0][0] == mark and board[1][0] == mark and board[2][0] == mark:
        return True
    if board[0][1] == mark and board[1][1] == mark and board[2][1] == mark:
        return True
    if board[0][2] == mark and board[1][2] == mark and board[2][2] == mark:
        return True
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    else:
        return False


def check_for_draw(board):
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == " ":
                return False
    return True


def play_game(board):
    welcome(board)
    initialise_board(board)
    draw_board(board)
    mark = "X"
    while check_for_win(board, mark) == False and check_for_draw(board) == False:

        get_player_move(board)
        draw_board(board)
        mark = "X"
        check_for_win(board, mark)
        if check_for_win(board, mark) == True:
            draw_board(board)
            print("Player wins.")
            print("End of game.")
            print("")
            return 1
        elif check_for_win(board, mark) == False:
            check_for_draw(board)
            if check_for_draw(board) == True:
                draw_board(board)
                print("Draw.")
                print("End of game.")
                print("")
                return 0

        choose_computer_move(board)
        draw_board(board)
        mark = "O"
        check_for_win(board, mark)
        if check_for_win(board, mark) == True:
            draw_board(board)
            print("Computer wins.")
            print("End of game.")
            print("")
            return -1
        elif check_for_win(board, mark) == False:
            check_for_draw(board)
            if check_for_draw(board) == True:
                draw_board(board)
                print("Draw.")
                print("End of game.")
                print("")
                return 0


def menu():
    menu = """Enter one of the following options:
    \t 1 - Play the game
    \t 2 - Save your score in the leaderboard
    \t 3 - Load and display the leaderboard
    \t q - End the program
    """
    print(menu)
    choice = input("1, 2, 3 or q: ")
    print("")
    return choice


def load_scores():
    file = open("leaderboard.txt", "r")
    s = file.read()
    leaders = json.loads(s)
    file.close()
    return leaders


def save_score(score):
    name = input("Enter your name: ")
    print("")
    leaders = load_scores()
    if name in leaders:
        leaders[name] += score
    else:
        leaders[name] = score
    file = open('leaderboard.txt', 'w')
    json.dump(leaders, file)
    return


def display_leaderboard(leaders):
    print("LEADERBOARD")
    for key in leaders.keys():
        print(key, ":", leaders[key])
    print("")
