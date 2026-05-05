"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head
        
        curNode = head
        while curNode:
            tmp = Node(curNode.val)
            tmp.next = curNode.next
            curNode.next = tmp
            curNode = tmp.next

        newHead =  head.next

        # Now assign the random values

        curNode = head

        while curNode:
            if curNode.random:
                curNode.next.random = curNode.random.next # This points to the copied node of the random node

            curNode = curNode.next.next


        # Now we remove older elements

        curNode = head

        while curNode:
            tmp = curNode.next
            curNode.next = tmp.next
            if tmp.next:
                tmp.next = tmp.next.next

            curNode = curNode.next

        return newHead
