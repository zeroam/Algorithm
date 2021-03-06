from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_tree_node(l: List[int]) -> TreeNode:
    if len(l) == 0:
        return None

    node = TreeNode(l[0])
    queue = [node]
    i = 1
    while i < len(l):
        cur_node = queue.pop(0)

        num = l[i]
        i += 1
        if num:
            left = cur_node.left = TreeNode(num)
            queue.append(left)

        num = l[i] if i < len(l) else None
        i += 1
        if num:
            right = cur_node.right = TreeNode(num)
            queue.append(right)

    return node


def inorder_traverse(root: TreeNode) -> List[int]:
    if root is None:
        return []

    return inorder_traverse(root.left) + [root.val] + inorder_traverse(root.right)


def listnode_to_list(head: ListNode) -> List[int]:
    ret = []
    while head:
        ret.append(head.val)
        head = head.next

    return ret


def list_to_listnode(l: List[int]) -> ListNode:
    dummy = head = ListNode()
    for num in l:
        head.next = ListNode(num)
        head = head.next

    return dummy.next
