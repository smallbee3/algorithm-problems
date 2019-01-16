"""
5_shapeArea

Below we will define an n-interesting polygon.
Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1.
An n-interesting polygon is obtained by taking the n - 1-interesting polygon
and appending 1-interesting polygons to its rim, side by side.
You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

Example

For n = 2, the output should be
shapeArea(n) = 5;
For n = 3, the output should be
shapeArea(n) = 13.

"""
"""
181207

Time : 10 min

Subject - Problem that needs mathematical thinking

"""

# 1
# 1 + 1*4
# 1 + 1*4 + 2*4
# ...


def shapeArea(n):
    output = 0
    for i in range(1, n+1):
        if i == 1:
            output += 1
        else:
            output += (i-1) * 4
    return output


# ret = shapeArea(1)
# print(ret)

# ret = shapeArea(2)
# print(ret)
#
# ret = shapeArea(3)
# print(ret)
#
ret = shapeArea(4)
print(ret)
