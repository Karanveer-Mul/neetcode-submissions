# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        
        # Now we have middle of list in slow
        sec_half = slow.next
        slow.next = None # Broke off the list

        curNode = sec_half
        prev = None

        while curNode:
            tmp = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = tmp

        # Now prev is the reversed half list
        sec_half = prev

        # we can now merge
        newList = head

        while sec_half:
            tmp1 = newList.next
            tmp2 = sec_half.next

            newList.next = sec_half
            sec_half.next = tmp1

            newList = tmp1
            sec_half = tmp2

