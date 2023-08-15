

"""
6. Playlist

A Youtube Playlist is considered a repeating playlist if all videos contain a reference
to a next video and the last video on the playlist points to the first video.
Otherwise, the playlist will end with the last video.
Implement a function “is_repeating_playlist” that, efficiently with respect to time used,
returns true if a playlist is repeating or false if it is not.

For example, the following code prints [“A”, “B”] as playlist is repeating.

first = Video("A")
second = Video("B")
first.next_video(second);
second.next_video(first);
print(first.is_repeating_playlist())

Otherwise, print “False” if playlist is not repeating.

"""


"""
* Subject - linked list

* Learning
    1. Use a hash table for a time-efficient problem

    2. The value of hashtable could work as a flag (1, 0)

"""

"""
class Video:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_video(self, video):
        self.next = video

    def is_repeating_playlist(self):
        # :returns: (bool) True if the playlist is repeating, False if not.
        pass


if __name__ == "__main__":
    first = Video("Hello World")
    second = Video("Why Python is So Popular")

    first.next_video(second);
    second.next_video(first);

    print(first.is_repeating_playlist())
"""

# Q1 Sovle the problem with regard to time efficiency

# 02 Using Ordered Dict?

# 03 Tell me the time complexity of the code


# Solution

from collections import OrderedDict


class Video:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_video(self, video):
        self.next = video

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """

        # 1) List
        # 18 min
        first_video = self
        curr_video = self

        playlist_list = []

        while True:
            playlist_list.append(curr_video.name)
            if not curr_video.next:
                return False
            elif curr_video.next.name == first_video.name:
                break
            elif curr_video.next.name in playlist_list and curr_video.next.name != first_video.name:
                return False
            curr_video = curr_video.next

        return playlist_list

    def is_repeating_playlist2(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """

        # 2) dict (efficiently with respect to time used)
        # 5 min
        first_video = self
        curr_video = self

        # playlist_dict = dict()
        playlist_dict = OrderedDict()

        while True:
            playlist_dict[curr_video.name] = 1
            if not curr_video.next:
                return False
            elif curr_video.next.name == first_video.name:
                break
            elif playlist_dict.get(curr_video.next.name) and curr_video.next.name != first_video.name:
                return False
            curr_video = curr_video.next

        playlist_list = list(playlist_dict.keys())
        return playlist_list


if __name__ == "__main__":
    first = Video("A")
    second = Video("B")
    third = Video("C")
    fourth = Video("D")

    first.next_video(second)
    second.next_video(third)
    third.next_video(fourth)
    fourth.next_video(first)
    print('Test I')
    print('1) ', first.is_repeating_playlist())
    print('2) ', first.is_repeating_playlist2())

    first.next_video(second)
    second.next_video(third)
    third.next_video(fourth)
    fourth.next_video(None)
    print('Test II')
    print('1) ', first.is_repeating_playlist())
    print('2) ', first.is_repeating_playlist2())

    first.next_video(second)
    second.next_video(third)
    third.next_video(fourth)
    fourth.next_video(second)
    print('Test III')
    print('1) ', first.is_repeating_playlist())
    print('2) ', first.is_repeating_playlist2())
