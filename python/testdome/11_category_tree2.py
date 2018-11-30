
# BEST PRACTICE
# https://www.savour-it.com/posts/2018-01-04-hyper-connect1/


class CategoryTree():
    categories = {}  # Define global variable for tree.

    def add_category(self, category, parent):
        # Validate unique of the name of category.
        if category in CategoryTree.categories:
            raise KeyError('The name of category already exists')
        # This creates each node of category in oneline,
        # even if it doesn't have children, it will have empty list.
        CategoryTree.categories[category] = []
        if parent is not None:
            # Get parent category
            parent = CategoryTree.categories[parent]
            parent.append(category)

    def get_children(self, parent):
        return CategoryTree.categories[parent]


c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')

# Keyerror 1 - duplicate
# c.add_category('C', 'A')

# Keyerror 2 - no parent
c.add_category('D', 'E')

# KeyError 3 - unique name
c.add_category('D', 'C')
c.add_category('D', 'B')

# Simple case
c.add_category('G', 'B')
c.add_category('H', 'B')
c.add_category('F', 'E')


print(','.join(c.get_children('A') or []))
print(','.join(c.get_children('B') or []))
