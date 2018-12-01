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


* Subject - Comparing with three options

* Learning
    1. Do coding as you write a pseudo code(inner function)
    2. The understanding of new function e.g Counter()
    3. Mistake when make a new sorted list by 'insert' function

"""


from collections import Counter
from collections import OrderedDict


# class LeagueTable:
#     def __init__(self, players):
#         self.standings = OrderedDict([(player, Counter()) for player in players])
#
#     def record_result(self, player, score):
#         self.standings[player]['games_played'] += 1
#         self.standings[player]['score'] += score
#
#     def player_rank(self, rank):
#
#         def compare_player(i, j):
#
#             if self.standings[i]['score'] > self.standings[j]['score']:
#                 return i
#             elif self.standings[i]['score'] < self.standings[j]['score']:
#                 return j
#             else:
#
#                 if self.standings[i]['games_played'] < self.standings[j]['games_played']:
#                     return i
#                 elif self.standings[i]['games_played'] > self.standings[j]['games_played']:
#                     return j
#                 else:
#
#                     player_list = list(self.standings.keys())
#                     if player_list.index(i) < player_list.index(j):
#                         return i
#                     else:
#                         return j
#
#         rank_list = []
#         for i in self.standings.keys():
#             if rank_list == []:
#                 rank_list.insert(0, i)
#             else:
#                 for idx, j in enumerate(rank_list):
#                     result = compare_player(i, j)
#                     if result == i:
#                         rank_list.insert(idx, i)
#                         break
#
#                     # The missing point where makes IndexError
#                     elif idx+1 == len(rank_list):
#                         rank_list.insert(idx+1, i)
#                         break
#
#         return rank_list[rank-1]
#
#
# table = LeagueTable(['Mike', 'Chris', 'Arnold'])
# table.record_result('Mike', 3)
# table.record_result('Mike', 6)
# table.record_result('Arnold', 7)
# table.record_result('Arnold', 2)
# table.record_result('Chris', 6)
# print(table.player_rank(1))


"""
181111 Review

Time : 35 min
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

    def compare_player(self, i, j):
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
                i_idx = list(self.standings.keys()).index(i)
                j_idx = list(self.standings.keys()).index(j)
                # if i_idx < j_idx:
                #     return i
                # else:
                #     return j
                return i if i_idx < j_idx else j

    def player_rank(self, rank):
        rank_list = [list(self.standings.keys())[0]]
        for i in list(self.standings.keys())[1:]:
            for idx, j in enumerate(rank_list):
                if self.compare_player(i, j) == i:
                    rank_list.insert(idx, i)
                    break
                if idx == len(rank_list)-1:
                    rank_list.insert(idx+1, i)
                    break

        return rank_list[rank-1]


table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))


"""
181129 Review 2

Time : 60 min
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

    def compare_score(self, i, j):

        if self.standings[i]['score'] > self.standings[j]['score']:
            return i
        elif self.standings[i]['score'] < self.standings[j]['score']:
            return j
        else:
            return 'tie'

    def compare_games_played(self, i, j):
        if self.standings[i]['games_played'] < self.standings[j]['games_played']:
            return i
        elif self.standings[i]['games_played'] > self.standings[j]['games_played']:
            return j
        else:
            return 'tie'

    def compare_order(self, i, j):
        keys_list = list(self.standings.keys())

        if keys_list.index(i) < keys_list.index(j):
            return i
        return j

    # 181129
    # * Early exit by 'continue' is not available
    # Because the last element cannot be inserted to the list

    # def player_rank(self, rank):
    #     rank_list = []
    #     for i in self.standings:
    #         if not rank_list:
    #             rank_list.append(i)
    #             continue
    #
    #         for idx, j in enumerate(rank_list):
    #             # score
    #             ret = self.compare_score(i, j)
    #             if ret == j:
    #                 continue
    #             if ret == i:
    #                 rank_list.insert(idx, i)
    #                 break
    #
    #             ret = self.compare_games_played(i, j)
    #             # games_played
    #             if ret == j:
    #                 continue
    #             if ret == i:
    #                 rank_list.insert(idx, i)
    #                 break
    #
    #             # order
    #             ret = self.compare_order(i, j)
    #             if ret == i:
    #                 rank_list.insert(idx, i)
    #                 break
    #
    #     return rank_list[rank-1]

    def player_rank(self, rank):
        rank_list = []
        for i in self.standings:
            if not rank_list:
                rank_list.append(i)
                continue

            for idx, j in enumerate(rank_list):
                # score
                ret = self.compare_score(i, j)
                if ret == i:
                    rank_list.insert(idx, i)
                    break

                elif ret == 'tie':
                    # games_played
                    ret = self.compare_games_played(i, j)
                    if ret == i:
                        rank_list.insert(idx, i)
                        break

                    elif ret == 'tie':
                        # order
                        ret = self.compare_order(i, j)
                        if ret == i:
                            rank_list.insert(idx, i)
                            break

            # missing point
            if idx == len(rank_list)-1:
                rank_list.insert(idx+1, i)

        return rank_list[rank-1]


table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 1)
print(table.player_rank(1))













