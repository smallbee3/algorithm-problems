
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
