
# 02 Ice Cream Machine

# Implement the IceCreamMachine's scoops method so that it returns all combinations of
# one ingredient and one topping.
# If there are no ingredients or toppings, the method should return an empty list.
# For example, IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops()
# should return [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].

"""
Time: 24 min
Tests: 4 pass / 0 fail
  Example case: Correct answer
  Various ingredients and one topping: Correct answer
  Various ingredients and toppings: Correct answer
  No ingredients and no toppings: Correct answer
"""


class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):

        icecream_with_toppings = []

        """
        Didn't read the question carefully!
        """
        # for i in self.ingredients:
        #     icecream_with_toppings.append([i])
        #
        # for j in icecream_with_toppings:
        #     for k in self.toppings:
        #         j.append(k)

        """
        Key point : decide the order of nested for loop (toppings -> ingredients)
        """
        for i in self.toppings:
            for j in self.ingredients:
                icecream_with_toppings.append([j, i])

        return icecream_with_toppings


# icecream = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
icecream = IceCreamMachine(["vanilla", "chocolate"], ["sauce1", "sauce2", "sauce3"])
print(icecream.scoops())
