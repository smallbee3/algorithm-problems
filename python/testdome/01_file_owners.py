
# 01 File Owners

# Implement a group_by_owners function that:

# * Accepts a dictionary containing the file owner name for each file name.
# * Returns a dictionary containing a list of file names for each owner name, in any order.

# For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
# the group_by_owners function should return
# {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

"""
Time: 10.41 min
Tests: 3 pass / 0 fail
  Example case: Correct answer
  Each owner has a single file: Correct answer
  Various files: Correct answer
"""


class FileOwners:

    @staticmethod
    def group_by_owners(files):

        result_dict = {}

        # Make a list value
        for i in files:
            owner = files[i]
            result_dict[owner] = []

        # Input file into the list
        for i, j in files.items():
            print(i, j)
            result_dict[j].append(i)

        return result_dict


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))