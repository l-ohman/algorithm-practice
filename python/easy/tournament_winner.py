# easy, array/hashmap

def tournamentWinner(competitions, results):
    highest_score = 0
    winning_team = ""
    scores = {}

    for i in range(len(competitions)):
        winner = competitions[i][0] if results[i] == 1 else competitions[i][1]
        if winner not in scores:
            scores[winner] = 0
        scores[winner] += 3

        if scores[winner] > highest_score:
            highest_score = scores[winner]
            winning_team = winner
    return winning_team
