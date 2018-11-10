"""
9. League Table

The LeagueTable class tracks the score of each player in a league.
After each game, the player records their score with the record_result function.

The player's rank in the league is calculated using the following logic:

1. The player with the highest score is ranked first (rank 1).
   The player with the lowest score is ranked last.
2. If two players are tied on score, then the player who has played the fewest games
   is ranked higher.
3. If two players are tied on score and number of games played,
   then the player who was first in the list of players is ranked higher.

Implement the player_rank function that returns the player at the given rank.
For example:

table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))

All players have the same score. However, Arnold and Chris
have played fewer games than Mike, and as Chris is before
Arnold in the list of players, he is ranked first. Therefore, the
code above should display "Chris".


Time : (more than) 60 min
Tests: 4 pass / 0 fail
  Example case: Correct answer
  Players have different scores: Correct answer
  Players tied by score: Correct answer
  Players tied by games played: Correct answer
"""


from collections import Counter
from collections import OrderedDict


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):

        def compare_player(i, j):

            if self.standings[i]['score'] > self.standings[j]['score']:
                return i
            elif self.standings[i]['score'] < self.standings[j]['score']:
                return j
            else:

                if self.standings[i]['games_played'] < self.standings[j]['games_played']:
                    return i
                elif self.standings[i]['games_played'] > self.standings[j]['games_played']:
                    return j
                else:

                    player_list = list(self.standings.keys())
                    if player_list.index(i) < player_list.index(j):
                        return i
                    else:
                        return j

        rank_list = []
        for i in self.standings.keys():
            if rank_list == []:
                rank_list.insert(0, i)
            else:
                for idx, j in enumerate(rank_list):
                    result = compare_player(i, j)
                    if result == i:
                        rank_list.insert(idx, i)
                        break

                    # The missing point where makes IndexError
                    elif idx+1 == len(rank_list):
                        rank_list.insert(idx+1, i)
                        break

        return rank_list[rank-1]


table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 3)
table.record_result('Mike', 6)
table.record_result('Arnold', 7)
table.record_result('Arnold', 2)
table.record_result('Chris', 6)
print(table.player_rank(1))
