# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], my_history=[]):
    if prev_play == "":
        my_history.append('R')
        return 'R'

    response = {'R':'S', 'P':'R', 'S':'P'}
    next_play = response[my_history[-1]]
    my_history.append(next_play)
    return next_play

    # if my_history[-1] == 'R':
    #     my_history.append('S')
    #     return 'S'
    # elif my_history[-1] == 'P':
    #     my_history.append('R')
    #     return 'R'
    # elif my_history[-1] == 'S':
    #     my_history.append('P')
    #     return 'P'
