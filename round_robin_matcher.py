import numpy as np
from random import randint


def random_games(team1, team2):
    with open("games.txt", "w") as out:
        n = len(team1)
        board = np.array([[(i + j) % n for i in range(n)] for j in range(n)])

        np.random.shuffle(board)
        board = board.T
        np.random.shuffle(board)

        gametags = np.array([f"Game{i+1}" for i in range(n)])
        games = np.array([[(team1[i], team2[board[i, j]]) for i in range(n)] for j in range(n)])
        went_first = np.array([0 for _ in range(n)])
        went_second = np.array([0 for _ in range(n)])

        first_team_members = np.arange(0, n)
        np.random.shuffle(first_team_members)

        for i in range(n):
            print(f"{gametags[i]:^45}", file=out)
            for j in first_team_members:
                s = randint(0, 1)
                if s == 0:
                    if went_second[j] != 4:
                        games[i, j, 0], games[i, j, 1] = games[i, j, 1], games[i, j, 0]
                        went_second[j] += 1
                    else:
                        went_first[j] += 1
                else:
                    if went_first[j] != 4:
                        went_first[j] += 1
                    else:
                        games[i, j, 0], games[i, j, 1] = games[i, j, 1], games[i, j, 0]
                        went_second[j] += 1
                print(f"{games[i, j, 0]:^20}{'-':^5}{games[i, j, 1]:^20}", file=out)
            print(file=out)


def main():
    home = ["a", "b", "c", "d", "e", "f", "g", "h"]
    vis = ["0", "1", "2", "3", "4", "5", "6", "7"]

    if len(home) != len(vis):
        raise ValueError("The teams need to be of the same length!")

    random_games(home, vis)


if __name__ == "__main__":
    main()

