import random
"""
This program execute a given number of runs of 
'Rock, Paper, Scissors' game and returns stats about it.
"""

choices = ['paper', 'rock', 'scissors']
winning = [('paper', 'rock'), ('rock', 'scissors'), ('scissors', 'paper')]


def run():
    """INPUT: no input.
       OUTPUT: string.
       The function randomly choose and returns a winner"""
    game = (random.choice(choices), random.choice(choices))
    if game not in winning:
        if game[0] == game[1]:
            return 'draw'
        else:
            return 'p2'
    else:
        return 'p1'


def counter(runs):
    """INPUT: integer; number of runs.
       OUTPUT: integers; number of wins per player and draws.
    The function appends, counts and returns each run's result."""
    results = []
    p1, p2, draw = (0, 0, 0)
    for _ in range(runs):
        results.append(run())
    for item in results:
        if item == 'p1':
            p1 += 1
        if item == 'p2':
            p2 += 1
        if item == 'draw':
            draw += 1

    return p1, p2, draw


def stats():
    """INPUT: no input.
       OUTPUT: strings; stats about the simulation.
       The function calculates and displays the stats."""
    p1_wins, p2_wins, draws = counter(num_of_runs)
    tot_wins = p1_wins + p2_wins + draws
    perc_p1 = (p1_wins / tot_wins) * 100
    perc_p2 = (p2_wins / tot_wins) * 100
    perc_draws = (draws / tot_wins) * 100
    print(f"After executing {num_of_runs} runs:")
    print("Player 1: {} wins {} %".format(p1_wins, round(perc_p1)))
    print("Player 2: {} wins {} %".format(p2_wins, round(perc_p2)))
    print("Draws   : {}      {} %.".format(draws, round(perc_draws)))


def validate_input(msg):
    while True:
        try:
            user_input = int(input(msg))
        except ValueError:
            print("Input not valid!")
        else:
            return user_input


if __name__ == "__main__":
    num_of_runs = validate_input("Please enter a number of simulation: ")
    stats()
