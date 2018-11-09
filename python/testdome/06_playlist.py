
# 06 Playlist

# A playlist is considered a repeating playlist if any of the songs contain a reference
# to a previous song in the playlist.
# Otherwise, the playlist will end with the last song which points to None.
# Implement a function is_repeating_playlist that, efficiently with respect to time used,
# returns true if a playlist is repeating or false if it is not.

# For example, the following code prints "True" as both songs point to each other.


# first = Song("Hello")
# second = Song("Eye of the tiger")
#
# first.next_song(second);
# second.next_song(first);
#
# print(first.is_repeating_playlist())


"""
Time: 48 min
Tests : 3 pass / 1 fail (Time limit exceeded)
"""

import time


# def my_timer(original_function):
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = original_function(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{}함수가 실행된 총 시간: {}초'.format(original_function.__name__, t2))
#         return result
#     return wrapper


class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    """
    1) Didn't read the question carefully!
    """
    # def is_repeating_playlist(self):
    #     """
    #     :returns: (bool) True if the playlist is repeating, False if not.
    #     """
    #     first_name = self.name
    #
    #     while True:
    #         if self.next is None:
    #             return False
    #
    #         self = self.next
    #
    #         if first_name == self.name:
    #             return True

    """
    2) Wrong placement of 'name_list.append(self.name)'
    """

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        name_list = []

        while True:
            if self.name in name_list:
                return True
            if self.next is None:
                return False
            name_list.append(self.name)
            self = self.next


first = Song("A")
second = Song("B")
third = Song("C")
fourth = Song("D")

first.next_song(second)
second.next_song(third)
third.next_song(fourth)
# fourth.next_song(third)
fourth.next_song(second) # -> infinite loop


time_a = time.time()
print(first.is_repeating_playlist())
running_time = time.time() - time_a
print(running_time)