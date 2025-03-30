def player(prev_play, opponent_history=[], my_history=[], pattern_found=[False], counter=[0]):
    if prev_play == "":
        my_history.append('R')
        return 'R'

    if opponent_history == "":
        opponent_history.append("R")
    opponent_history.append(prev_play)

    quincy_pattern = ["R", "P", "P", "S", "R"]
    if not pattern_found[0]:
        i = -1
        for j in reversed(quincy_pattern):
            if i >= -5 and len(opponent_history) >= 5 and j == opponent_history[i]:
                i -= 1
                pattern_found[0] = True
            else:
                pattern_found[0] = False
                break
    if pattern_found[0]:
        counter[0] += 1
        choices_vs_quincy = ["P", "P", "S", "S", "R"]
        return choices_vs_quincy[counter[0] % len(choices_vs_quincy)]

    response = {'R':'S', 'P':'R', 'S':'P'}
    next_play = response[my_history[-1]]
    my_history.append(next_play)
    return next_play