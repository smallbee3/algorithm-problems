"""
6_almostIncreasingSequence

Given a sequence of integers as an array, determine whether
it is possible to obtain a strictly increasing sequence
by removing no more than one element from the array.


Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed
in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2].
Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

"""
"""
181204

Time : 60 min

Subject : Find the exception case and make it as early exit from the problem

Leaning
    1. early exit adjusted pretty well
    2. Think two cases at one situation

"""


def almost_increasing_sequence(sequence):

    count_of_decreasing = 0
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            count_of_decreasing += 1
            # if i != len(sequence)-2 and sequence[i] > sequence[i+2]:

            # [10, 1, 2, 3, 4, 5]
            if i == 0:
                continue

            # case when remove sequence[i+1
            if i != 0 and sequence[i-1] < sequence[i+1]:
                continue

            # case when remove sequence[i]
            if i != len(sequence)-2 and sequence[i] < sequence[i+2]:
                continue

            # [3, 5, 67, 98, 3]
            if i == len(sequence)-2 and sequence[i-2] < sequence[i-1]:
                continue

            count_of_decreasing += 1

    if count_of_decreasing > 1:
        return False
    return True


# sequence = [40, 50, 60, 10, 20, 30]
# sequence = [1, 1]
# sequence = [1, 3, 2, 1]
# sequence = [1, 2, 1, 2]
# sequence = [1, 2, 5, 3, 5]
sequence = [3, 5, 67, 98, 3]

result = almost_increasing_sequence(sequence)
print(result)
