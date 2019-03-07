# -*- coding utf-8 -*-


# 定义二叉树数据结构
class TreeNode():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder_traversal(root):
    if root is None:
        return

    print(root.value)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def inorder_traversal(root):
    if root is None:
        return

    inorder_traversal(root.left)
    print(root.value)
    inorder_traversal(root.right)


def postorder_traversal(root):
    if root is None:
        return

    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.value)

tree = TreeNode('D', TreeNode('B', TreeNode('A'), TreeNode('C')), TreeNode('E', right=TreeNode('G', TreeNode('F'))))

print('preoder')
preorder_traversal(tree)
print('inoder')
inorder_traversal(tree)
print('postoder')
postorder_traversal(tree)