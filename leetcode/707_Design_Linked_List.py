from typing import Optional


class ListNode(object):
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def _get_node(self, index: int) -> Optional[ListNode]:
        if index < 0 or index >= self.size:
            return None

        cur_index = 0
        cur_node = self.head
        while cur_node and cur_index < index:
            cur_index += 1
            cur_node = cur_node.next

        return cur_node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self._get_node(index)
        return node.val if node else -1


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # check add at first
        if index == 0:
            temp_node = self.head
            self.head = ListNode(val)
            self.head.next = temp_node
            self.size += 1
            return

        prev_node = self._get_node(index - 1)
        if prev_node is None:
            return

        cur_node = ListNode(val)
        next_node = prev_node.next

        prev_node.next = cur_node
        cur_node.next = next_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # check delete first node
        if index == 0 and self.head:
            self.head = self.head.next
            self.size -= 1
            return

        prev_node = self._get_node(index - 1)
        if prev_node is None:
            return

        cur_node = prev_node.next
        if cur_node is None:
            return
        next_node = cur_node.next

        prev_node.next = next_node
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
