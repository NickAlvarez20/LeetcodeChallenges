class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        # Recursively prints the tree with indentation
        indent = " " * level
        print(f"{indent} --- {self.data}")
        for child in self.children:
            child.print_tree(level + 1)


# Example: Building a company hierarchy
root = TreeNode("CEO")
cto = TreeNode("CTO")
cfo = TreeNode("CFO")

root.add_child(cto)
root.add_child(cfo)

# Adding more layers
cto.add_child(TreeNode("Dev Lead"))
cto.add_child(TreeNode("QA Lead"))

root.print_tree()
