# -*- coding utf-8 -*-

"""
已知 前序遍历与中序遍历， 求后序遍历
必须有中序遍历才能构建另一个二叉树
"""

list_pre = list('DBACEGF')
list_in = list('ABCDEFG')
list_post = []



def find_postorder(list_pre, list_in, list_post):
    if len(list_pre) == 0:
        return
    if len(list_pre) == 1:
        list_post.append(list_pre[0])
        return
    root = list_pre[0]
    # index 返回列表元素的索引
    n = list_in.index(root)
    # [1:n+1]为左子树，其中n为中序中root的index
    #  递归的从中序前序构建后续遍历
    find_postorder(list_pre[1:n+1], list_in[:n], list_post)
    find_postorder(list_pre[n+1:], list_in[n:], list_post)
    # 后续遍历根节点在后
    list_post.append(root)

find_postorder(list_pre, list_in, list_post)
print(list_post)