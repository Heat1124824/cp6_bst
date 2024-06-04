class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MyBST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return self.root
        
        cur = self.root
        while cur:
            if cur.val > val:
                if cur.left is None:
                    cur.left = Node(val)
                    return cur.left
                cur = cur.left
            elif cur.val < val:
                if cur.right is None:
                    cur.right = Node(val)
                    return cur.right
                cur = cur.right
            else:
                return None  # 數值已存在
        return None

    def find_max(self, root):
        if root is None:
            return None
        while root.right:
            root = root.right
        return root.val

    def find_min(self, root):
        if root is None:
            return None
        while root.left:
            root = root.left
        return root.val

    def max_depth(self, root):
        if root is None:
            return 0
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        return max(left_depth, right_depth) + 1

bst = MyBST()
values = [10, 5, 15, 3, 7, 17, 12, 6]
for val in values:
    bst.insert(val)

print("BST中的最大值: ", bst.find_max(bst.root))
print("BST中的最小值: ", bst.find_min(bst.root))
print("BST的最大深度: ", bst.max_depth(bst.root))
