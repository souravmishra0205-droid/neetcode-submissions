# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        reverseNode = ListNode(head.val)
        while head.next:
            head = head.next
            val = head.val
            newNode = ListNode(val)
            newNode.next = reverseNode
            reverseNode = newNode
        return reverseNode
        