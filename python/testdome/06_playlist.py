"""
6. Playlist

A playlist is considered a repeating playlist if any of the songs contain a reference
to a previous song in the playlist.
Otherwise, the playlist will end with the last song which points to None.
Implement a function is_repeating_playlist that, efficiently with respect to time used,
returns true if a playlist is repeating or false if it is not.

For example, the following code prints "True" as both songs point to each other.


first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second);
second.next_song(first);

print(first.is_repeating_playlist())


Time: 48 min
Tests : 3 pass / 1 fail (Time limit exceeded)


* Subject - linked list

* Learning
    1. Use hash table on problem with the time efficiency issue

    2. The value of hashtable could work as a flag (1, 0)

"""

# import time
#
#
# # def my_timer(original_function):
# #     def wrapper(*args, **kwargs):
# #         t1 = time.time()
# #         result = original_function(*args, **kwargs)
# #         t2 = time.time() - t1
# #         print('{}함수가 실행된 총 시간: {}초'.format(original_function.__name__, t2))
# #         return result
# #     return wrapper
#
#
# class Song:
#     def __init__(self, name):
#         self.name = name
#         self.next = None
#
#     def next_song(self, song):
#         self.next = song
#
#     """
#     1) Didn't read the question carefully!
#     """
#     # def is_repeating_playlist(self):
#     #     """
#     #     :returns: (bool) True if the playlist is repeating, False if not.
#     #     """
#     #     first_name = self.name
#     #
#     #     while True:
#     #         if self.next is None:
#     #             return False
#     #
#     #         self = self.next
#     #
#     #         if first_name == self.name:
#     #             return True
#
#     """
#     2) 1 fail : Performance test on a large playlist: Time limit exceeded
#     """
#
#     def is_repeating_playlist(self):
#         """
#         :returns: (bool) True if the playlist is repeating, False if not.
#         """
#         name_list = []
#
#         while True:
#             if self.name in name_list:
#                 return True
#             if self.next is None:
#                 return False
#             name_list.append(self.name)
#             self = self.next
#
#
# first = Song("A")
# second = Song("B")
# third = Song("C")
# fourth = Song("D")
#
# first.next_song(second)
# second.next_song(third)
# third.next_song(fourth)
# # fourth.next_song(third)
# fourth.next_song(second)
#
# print(first.is_repeating_playlist())


"""
Time : 24.44 (min)
Tests: 4 pass / 0 fail
  Example case: Correct answer
  Song will repeat: Correct answer
  Song will not repeat: Correct answer
  Performance test on a large playlist: Correct answer
"""


class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        # 1) list : fail
        # song = self
        # played_songs = []
        #
        # while song:
        #     if song.name in played_songs:
        #         return True
        #     played_songs.append(song.name)
        #     song = song.next
        # return False

        # 2) dict : pass
        song = self
        played_songs = {}

        while song:
            if played_songs.get(song.name):
                return True

            played_songs[song.name] = 1
            song = song.next
        return False


first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second)
second.next_song(first)

print(first.is_repeating_playlist())


"""
181111 Review

Time : 15 (min)
Tests: 4 pass / 0 fail
  Example case: Correct answer
  Song will repeat: Correct answer
  Song will not repeat: Correct answer
  Performance test on a large playlist: Correct answer
"""


"""
181129 Review 2

Time : 5 (min)
Tests: 4 pass / 0 fail
  Example case: Correct answer
  Song will repeat: Correct answer
  Song will not repeat: Correct answer
  Performance test on a large playlist: Correct answer
"""


class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        # dict1 = {}
        # node = self
        # while node:
        #     if dict1.get(node.name):
        #         return True
        #     dict1[node.name] = 1
        #     node = node.next
        # return False

        # 190120
        adict = {}
        while self.next:
            if adict.get(self.name):
                return True
            else:
                adict[self.name] = 1
                self = self.next
        return False


# first = Song("Hello")
# second = Song("Eye of the tiger")
first = Song("A")
second = Song("B")
third = Song("C")
fourth = Song("D")

# first.next_song(second);
# second.next_song(first);

first.next_song(second)
second.next_song(second)
third.next_song(first)
fourth.next_song(first)

print(first.is_repeating_playlist())

"""
230810 Review 3

Time: 20 min
"""


class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        if not self or self.next is None:
            return False

        curr_song = self
        song_name_list = []

        while curr_song:
            song_name_list.append(curr_song.name)
            if curr_song.next and curr_song.next.name in song_name_list:
                return True
            curr_song = curr_song.next

        return False
