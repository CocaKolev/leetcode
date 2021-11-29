# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    fromStart= len(head)-n
    head[fromStart]
    
    
    return




removeNthFromEnd([3,4,5], 2)

x=ListNode(3)
x.next=ListNode(4)
x.next.next=ListNode(5)