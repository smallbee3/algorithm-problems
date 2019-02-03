import time


class Candies:
    @staticmethod
    def count_candies(starting_amount, new_every):

        if new_every == 0 or starting_amount < new_every:
            return starting_amount

        if new_every == 1:
            return float('inf')

        # current_amount = starting_amount
        # eaten_amount = 0
        #
        # while True:
        #     current_amount = current_amount - new_every + 1
        #     eaten_amount += new_every
        #     if current_amount < new_every:
        #         eaten_amount += current_amount
        #         break
        # return eaten_amount

        # n = 1
        # while True:
        #     if starting_amount - (new_every - 1) * n <= 0:
        #         final_amount = starting_amount - (new_every - 1) * (n - 1)
        #         break
        #     n += 1
        # return (n - 1) * new_every + final_amount

        n = starting_amount // (new_every - 1)
        left = starting_amount % (new_every - 1)

        # print()
        # print(n)
        # print(left)

        if left == 0:

            # Couldn't calculate with (n-1)th case
            # return (n - 1) * new_every + new_every

            return n * new_every - 1
        else:
            return n * new_every + left


print(Candies.count_candies(3, 2))
print(Candies.count_candies(10, 3))
print(Candies.count_candies(200, 4))
print(Candies.count_candies(555, 7))

str_time = time.time()
print(Candies.count_candies(10000000, 3))
duration_time = time.time() - str_time

print(duration_time)
# >> 5.9604644775390625e-06
# >> 0.00000596046447753906


# Exception 1 - new_every = 0
# print(Candies.count_candies(3, 0))

# Exception 2 - new_every = 1
# print(Candies.count_candies(3, 1))

# Exception 3 - starting_amount < new_every
# print(Candies.count_candies(1, 2))
