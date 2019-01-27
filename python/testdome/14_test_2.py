import time


class Candies:
    @staticmethod
    def count_candies(starting_amount, new_every):

        if new_every == 0 or starting_amount < new_every:
            return starting_amount

        if new_every == 1:
            return float('inf')

        current_amount = starting_amount
        eaten_amount = 0

        while True:
            current_amount = current_amount - new_every + 1
            eaten_amount += new_every
            if current_amount < new_every:
                eaten_amount += current_amount
                break
        return eaten_amount


print(Candies.count_candies(3, 2))
print(Candies.count_candies(10, 3))
print(Candies.count_candies(11, 3))
print(Candies.count_candies(12, 3))
print(Candies.count_candies(200, 4))
print(Candies.count_candies(555, 7))

str_time = time.time()
print(Candies.count_candies(10000000, 3))
duration_time = time.time() - str_time

print(duration_time)
# >> 0.6737668514251709


# Exception 1 - new_every = 0
# print(Candies.count_candies(3, 0))

# Exception 2 - new_every = 1
# print(Candies.count_candies(3, 1))

# Exception 3 - starting_amount < new_every
# print(Candies.count_candies(1, 2))


"""
181202 Review

Time : 30 min

Learning:
    1. Need break when inserting the node in the last loop into new sorted_list

"""


class Candies:
    @staticmethod
    def count_candies(starting_amount, new_every):

        # maximum = 0
        # while True:
        #     starting_amount = starting_amount - new_every + 1
        #     maximum += new_every
        #
        #     if starting_amount < new_every:
        #         maximum += starting_amount
        #         break

        if new_every == 1:
            return float('inf')

        # 181202 I missed the when new_every is '0' case
        # if new_every > starting_amount:
        if new_every == 0 or starting_amount < new_every:
            return starting_amount

        if not starting_amount % (new_every - 1):
            maximum = starting_amount // (new_every - 1) * new_every - 1
        else:
            maximum = starting_amount // (new_every - 1) * new_every + starting_amount % (new_every - 1)

        return maximum


print()
print(Candies.count_candies(3, 2))
print(Candies.count_candies(10, 3))
# print(Candies.count_candies(11, 3))
# print(Candies.count_candies(12, 3))
# print(Candies.count_candies(200, 4))
print(Candies.count_candies(555, 7))

# Exception 1
print(Candies.count_candies(3, 0))

# Exception 2
print(Candies.count_candies(3, 1))

# For the faster answer (option)
# print(Candies.count_candies(3, 7))
