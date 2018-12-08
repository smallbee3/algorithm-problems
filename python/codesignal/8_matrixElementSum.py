"""
8_matrixElementSum

After they became famous, the CodeBots all decided to move to a new building
and live together. The building is represented by a rectangular matrix of rooms.
Each cell in the matrix contains an integer that represents the price of the room.
Some rooms are free (their cost is 0), but that's probably because they are haunted,
so all the bots are afraid of them. That is why any room that is free or is located
anywhere below a free room in the same column is not considered suitable for the bots to live in.

Help the bots calculate the total price of all the rooms that are suitable for them.


Example

For
matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
the output should be
matrixElementsSum(matrix) = 9.

Here's the rooms matrix with unsuitable rooms marked with 'x':

[[x, 1, 1, 2],
 [x, 5, x, x],
 [x, x, x, x]]
Thus, the answer is 1 + 5 + 1 + 2 = 9.

For
matrix = [[1, 1, 1, 0],
          [0, 5, 0, 1],
          [2, 1, 3, 10]]
the output should be
matrixElementsSum(matrix) = 9.

Here's the rooms matrix with unsuitable rooms marked with 'x':

[[1, 1, 1, x],
 [x, 5, x, x],
 [x, 1, x, x]]
Note that the free room in the first row make the full column unsuitable for bots.

Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9.

"""
"""
181208

Time : 17 min

Subject - Consider two cases in one operation 
          (1 - sum, 2 - change the price of current room)

"""


def matrixElementsSum(matrix):

    price_sum = 0

    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         if matrix[i][j] == 0:
    #             for k in range(i, len(matrix)):
    #                 matrix[k][j] = 0
    #
    # I even gave up writing this code because it is already takes O(n³)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # row == 0
            if i == 0:
                price_sum += matrix[i][j]
                continue
            # if previous row was not free (This is possible because of the below code)
            if matrix[i-1][j] != 0:
                price_sum += matrix[i][j]
            # change the price of current room, matrix[i][j] for the next loop operation
            else:
                matrix[i][j] = 0

    print(matrix)
    return price_sum


# matrix = [[0, 1, 1, 2],
#           [0, 5, 0, 0],
#           [2, 0, 3, 3]]

matrix = [[1, 1, 1, 0],
          [0, 5, 0, 1],
          [2, 1, 3, 10]]


result = matrixElementsSum(matrix)
print(result)
