"""
4_adjacentElementsProduct

en an array of integers, find the pair of adjacent elements
that has the largest product and return that product.


Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.

"""
"""
181206

Subject - largest product

Learning
    1. "largest_product = 1" could make a problem

"""


def adjacentElementsProduct(inputArrary):

    largest_product = inputArrary[0] * inputArrary[1]
    for i in range(len(inputArrary)-1):
        product = inputArrary[i] * inputArrary[i+1]
        if product > largest_product:
            largest_product = product

    return largest_product
