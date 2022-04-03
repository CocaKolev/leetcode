from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head.next == None:
        return None
    mylist= []

    while head != None:
        mylist.append(head)
        head=head.next
    
    indexToRemove=len(mylist)-n

    if indexToRemove==0:
        return mylist[1]
    
    mylist[indexToRemove-1].next=mylist[indexToRemove].next
    
    return mylist[0]

def newListNode(nums):
    ln = ListNode(nums[0])
    ln2=ln
    for x in range(1,len(nums)):
        ln2.next=ListNode(nums[x])
        ln2=ln2.next
    return ln

def printListNode(node: ListNode):
    while node != None:
        print(node.val)
        node=node.next


printListNode(removeNthFromEnd(newListNode([2]),1))