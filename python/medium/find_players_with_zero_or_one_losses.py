# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/?envType=daily-question&envId=2024-01-15


# first attempt - beats 60% time, 83% space
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_counter = {}
        for match in matches:
            winner, loser = match[0], match[1]
            if winner not in loss_counter:
                loss_counter[winner] = 0
            if loser not in loss_counter:
                loss_counter[loser] = 0
            loss_counter[loser] += 1

        no_losses, one_loss = [], []
        for player in sorted(loss_counter.keys()):
            if loss_counter[player] == 0:
                no_losses.append(player)
            elif loss_counter[player] == 1:
                one_loss.append(player)

        return [no_losses, one_loss]
