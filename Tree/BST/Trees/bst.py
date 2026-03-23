class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    # If the tree is empty, return a new node
    if root is None:
        return BSTNode(val)

    # Otherwise, recur down the tree
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right), val

    return root


def search(root, target):
    # Base Cases: root is null or target is present at root
    if root is None or root.val == target:
        return root is not None

    # Target is greater than root's value
    if target > root.val:
        return search(root.right, target)

    # Target is smaller than root's value
    return search(root.left, target)


# Example Usage:
root = BSTNode(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

print(f"Is 40 in the tree? {search(root, 40)}")  # True
print(f"Is 90 in the tree? {search(root, 90)}")  # False
