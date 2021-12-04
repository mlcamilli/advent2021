from collections import Counter, OrderedDict

import numpy as np


def bingo():
    with open("input", "r") as f:
        data = f.read().split("\n\n")
    numbers = data[0].split(",")
    boards = []
    for board_data in data[1:]:
        board = np.array([row.strip().split() for row in board_data.split("\n") if row])
        answer_board = np.full((5, 5), False)
        boards.append((board, answer_board))

    winner, answer, final_number = find_winner(numbers, boards)
    x, y = np.where(answer == False)
    sum = 0
    for i in range(0, len(x)):
        sum += int(winner[x[i]][y[i]])
    print(f"Final Number {final_number}, Sum {sum}, Score {sum*int(final_number)}")


def find_winner(numbers, boards):
    for number in numbers:
        for board, answer in boards:
            x, y = np.where(board == number)
            for i in range(0, len(x)):
                answer[x[i]][y[i]] = True
                xcounter = Counter(answer[x[i]])
                ycounter = Counter(answer[:, y[i]])
                if xcounter[True] == 5 or ycounter[True] == 5:
                    return board, answer, number
    raise Exception("No Winner Found")


def find_winners(numbers, boards):
    winners = OrderedDict()
    for number in numbers:
        for n in range(0, len(boards)):
            if n not in winners:
                board, answer = boards[n]
                x, y = np.where(board == number)
                for i in range(0, len(x)):
                    answer[x[i]][y[i]] = True
                    xcounter = Counter(answer[x[i]])
                    ycounter = Counter(answer[:, y[i]])
                    if xcounter[True] == 5 or ycounter[True] == 5:
                        winners[n] = (board, answer)
        if len(winners) == len(boards):
            return winners, number


def bingo_last():
    with open("input", "r") as f:
        data = f.read().split("\n\n")
    numbers = data[0].split(",")
    boards = []
    for board_data in data[1:]:
        board = np.array([row.strip().split() for row in board_data.split("\n") if row])
        answer_board = np.full((5, 5), False)
        boards.append((board, answer_board))

    winners, final_number = find_winners(numbers, boards)
    loser_number = next(reversed(winners))
    loser, answer = winners[loser_number]
    x, y = np.where(answer == False)
    sum = 0
    for i in range(0, len(x)):
        sum += int(loser[x[i]][y[i]])
    print(f"Final Number {final_number}, Sum {sum}, Score {sum*int(final_number)}")


if __name__ == "__main__":
    bingo_last()
