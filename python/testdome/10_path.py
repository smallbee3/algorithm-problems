"""
10. Path

Write a function that provides change directory (cd) function
 for an abstract file system.

Notes:

Root path is '/'.
Path separator is '/'.
Parent directory is addressable as '..'.
Directory names consist only of English alphabet letters (A-Z and a-z).
The function should support both relative and absolute paths.
The function will not be passed any invalid paths.
Do not use built-in path-related functions.


For example:

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)

should display '/a/b/c/x'.


Time : 90 min
Tests: 3 pass / 1 fail
  Example case: Correct answer
  Selecting child directories: Correct answer
  Selecting parent directories: Correct answer
  Selecting complex paths: Wrong answer
"""


import re


class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):

        # Directory name validation (A-Z and a-z)

        # # Regex Study
        result1 = re.findall('[^./]', new_path.lower())
        result2 = re.findall('[^a-z]', new_path.lower())
        result2_2 = re.findall('[^a-zA-Z]', new_path)
        result3 = re.findall('[^a-z/.]', new_path.lower())

        # 1) Filter "Character", ".", "/"
        result3_2 = re.findall('[^a-zA-Z/.]', new_path)
        # if result3_2:
        #     return print('Directory names consist only of English alphabet letters (A-Z and a-z).')

        # 2) Cover the case '../x.abc'
        # slash_idx = new_path.index('/')
        # new_path_test = new_path[slash_idx:]
        # result4 = re.findall('[^a-zA-Z/]', new_path_test)
        # if result4:
        #     return print('Directory names consist only of English alphabet letters (A-Z and a-z).')

        # 3) Cover the case 'x.abc' or 'x.abc/etc'
        # if re.match('\.', new_path):
        #     slash_idx = new_path.index('/')
        #     new_path_for_test = new_path[slash_idx:]
        # else:
        #     new_path_for_test = new_path
        #
        # result5 = re.findall('[^a-zA-Z/]', new_path_for_test)
        # if result5:
        #     return print('Directory names consist only of English alphabet letters (A-Z and a-z).')

        # 4) Cover the case '..'
        if re.match('\.', new_path) \
                and re.findall('[^.]', new_path):

            slash_idx = new_path.index('/')
            new_path_for_test = new_path[slash_idx:]
        else:
            new_path_for_test = new_path

        result5 = re.findall('[^a-zA-Z/]', new_path_for_test)
        if result5 \
                and re.findall('[^.]', new_path):
            return print('Directory names consist only of English alphabet letters (A-Z and a-z).')

        # "/"
        if new_path.startswith('/'):
            self.current_path = new_path

        # ".."
        # elif new_path.startswith('..'):
        #     dir_list = self.current_path.split('/')
        #     dir_list = dir_list[1:]
        #     parent_path = dir_list[:len(dir_list)-1]
        #
        #     dir_list2 = new_path.split('/')
        #     child_path = dir_list2[1:]
        #
        #     self.current_path = '/' + '/'.join(parent_path + child_path)

        # ".. > 2"
        elif new_path.startswith('..'):

            dir_list2 = new_path.split('/')
            dot_num = len(dir_list2[0])
            child_path = dir_list2[1:]

            dir_list = self.current_path.split('/')
            dir_list = dir_list[1:]
            parent_path = dir_list[:len(dir_list)-dot_num+1]

            self.current_path = '/' + '/'.join(parent_path + child_path)

        # "."
        # elif new_path.startswith('.'):
        #     dir_list = self.current_path.split('/')
        #     parent_path = dir_list[1:]
        #
        #     dir_list2 = new_path.split('/')
        #     child_path = dir_list2[1:]
        #
        #     self.current_path = '/' + '/'.join(parent_path + child_path)
        #

        # "(child directory)"
        # elif re.match('\w', new_path):
        #     dir_list = self.current_path.split('/')
        #     parent_path = dir_list[1:]
        #
        #     child_path = new_path.split('/')
        #
        #     self.current_path = '/' + '/'.join(parent_path + child_path)

        # 'Code Refactored'

        # "." & "(child directory)"
        elif new_path.startswith('.') \
                or re.match('[a-zA-Z]', new_path):
            dir_list = self.current_path.split('/')
            parent_path = dir_list[1:]

            child_path = new_path.split('/')

            if new_path.startswith('.'):
                child_path = child_path[1:]

            self.current_path = '/' + '/'.join(parent_path + child_path)


path = Path('/a/b/c/d')

# Select parent directory
# path.cd('../x')
# path.cd('.../x')
# path.cd('..../x')
# path.cd('...../x')

# Select child directory
# path.cd('x')
# path.cd('./x')


# Exceptions 1

# path.cd('1x')
# path.cd('x1')
# path.cd('x*')
# path.cd('*x')


# Exceptions 2

# path.cd('x.abc')
# path.cd('x.abc/etc')
# path.cd('x.abc/etc/new')
# path.cd('./x.abc')
# path.cd('../x.abc')
# path.cd('.../x.abc')


# Exceptions 3

# path.cd('..')
# path.cd('...')
# path.cd('....')
# path.cd('.....')


print(path.current_path)
