class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.children = []

class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def is_empty(self):
        return self.root is None

    def insert(self,data,parent = None):
        new_node = TreeNode(data)
        if parent is None:
            if self.is_empty():
                self.root = new_node
            else:
                return ValueError("Can't add a root node if the Tree is not empty.")
        else:
            parent.children.append(new_node)
    
    def find(self,data):
        if self.is_empty():
            return None
        else:
            return self._find_node(self.root,data)
    
    def _find_node(self,current_node,data):
        if current_node.data == data:
            return current_node
        else:
            for child in current_node.children:
                found_node = self._find_node(child,data)
                if found_node:
                    return found_node
        return None
    
    def Display(self):
        if self.is_empty():
            print("Tree is empty.")
        else:
            self._display_node(self.root,0)

    def _display_node(self,current_node,level):
        print("  " * level + str(current_node.data))
        for child in current_node.children:
            self._display_node(child,level+1)

# Now testing :

# Creating a tree and inserting nodes:

tree = Tree()

# Inserting root node
tree.insert("A")

# Inserting child nodes
tree.insert("B", parent=tree.root)
tree.insert("C", parent=tree.root)
tree.insert("D", parent=tree.root)

# Inserting grandchildren nodes
node_b = tree.find("B")
tree.insert("E", parent=node_b)
tree.insert("F", parent=node_b)

node_d = tree.find("D")
tree.insert("G", parent=node_d)

# Displaying the tree
tree.Display()



# Finding a node in the tree:

# Find a node
found_node = tree.find("F")

# Check if node is found
if found_node:
    print("Node found:", found_node.data)
else:
    print("Node not found")


# Checking if the tree is empty:

# Check if tree is empty
if tree.is_empty():
    print("Tree is empty")
else:
    print("Tree is not empty")



# Extra Notes: 

'''
Tree:
- A tree is a hierarchical data structure that consists of nodes connected by edges.
- Each node in a tree can have zero or more child nodes, forming a parent-child relationship.
- The topmost node in a tree is called the root node, and each node can have any number of children.
- Nodes in a tree are organized in levels, with the root node at level 0 and subsequent levels determined by the distance from the root.
- Trees are commonly used to represent hierarchical relationships, such as file systems, organization structures, or family trees.

Code Explanation:
- insert(data, parent=None): Inserts a new node with the given data into the tree. If the parent is not provided, it adds the node as the root. If the parent is specified, it adds the node as a child of the parent node.
- _find_node(current_node, data): Recursively searches for a node with the given data starting from the current node. It returns the node if found, otherwise None.
- Display(): Displays the tree structure by recursively traversing and printing each node's data along with indentation to represent levels.
- is_empty(): Checks if the tree is empty by checking if the root node is None.

{Here I have used DFS to find data}

Note on Exception Usage:
- Exceptions are used in the code to handle specific cases or errors. For example, when trying to add a root node to a non-empty tree, a ValueError exception is raised to indicate that it is not allowed.

'''