"""
1. File Owners

Implement a group_by_owners function that:

* Accepts a dictionary containing the file owner name for each file name.
* Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
the group_by_owners function should return
{'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.


def group_by_owners(files):
    return None

if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))


Time: 10.41 min
Tests: 3 pass / 0 fail
  Example case: Correct answer
  Each owner has a single file: Correct answer
  Various files: Correct answer


* Subject - Swapping key and value of dict

* Learning
    1. Make value of dict as list to add more than one data
    2. The usage of method "items()"

"""


# class FileOwners:
#
#     @staticmethod
#     def group_by_owners(files):
#
#         result_dict = {}
#
#         # Make a list value
#         for i in files:
#             owner = files[i]
#             result_dict[owner] = []
#
#         # Input file into the list
#         for i, j in files.items():
#             print(i, j)
#             result_dict[j].append(i)
#
#         return result_dict
#
#
# files = {
#     'Input.txt': 'Randy',
#     'Code.py': 'Stan',
#     'Output.txt': 'Randy'
# }
# print(FileOwners.group_by_owners(files))


"""
181111 Review 1

Time: 5 min
Tests: 3 pass / 0 fail
  Example case: Correct answer
  Each owner has a single file: Correct answer
  Various files: Correct answer
"""


class FileOwners:
    @staticmethod
    def group_by_owners(files):
        new_dict = {}
        for k, v in files.items():
            if new_dict.get(v):
                new_dict[v].append(k)
            else:
                new_dict[v] = [k]
            # new_dict[v].append(k) if new_dict.get(v) else new_dict[v] = [k]
        return new_dict


files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
print(FileOwners.group_by_owners(files))


"""
181129 Review 2

Time: 5 min
Tests: 3 pass / 0 fail
  Example case: Correct answer
  Each owner has a single file: Correct answer
  Various files: Correct answer
"""


# class FileOwners:
#
#     @staticmethod
#     def group_by_owners(files):
#
#         dict = {}
#         for key in files:
#         #     value = files[key]
#         #     if dict.get(value):
#         #         dict[value].append(key)
#         #     else:
#         #         dict[value] = [key]
#
#             dict[files[key]] = dict[files[key]] + [key] if dict.get(files[key]) else [key]
#
#         return dict
#
#
# files = {
#     'Input.txt': 'Randy',
#     'Code.py': 'Stan',
#     'Output.txt': 'Randy'
# }
# print(FileOwners.group_by_owners(files))


"""
230807 Review 3

Time: 5.37 min
Code: The same as "Review 1"
"""
