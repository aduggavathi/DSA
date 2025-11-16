# Intersection of Two linked list brute force approach.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # TERA GENIUS SAFETY CHECK!
        if not headA or not headA.next or not headB or not headB.next:
            return None
            
        prevA = currA = headA
        prevB = currB = headB
        
        while True:
            while currA and currB:
                prevA = currA
                prevB = currB
                if prevA is prevB:
                    return prevA
                currA = currA.next
                currB = currB.next
            
            if currA:
                currB = headB
                prevB = None
            elif currB:
                currA = headA
                prevA = None
            else:
                break
        return None

# Intersection of Two linked list optimized approach.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        currA = headA
        currB = headB

        while currA != currB:

            if currA is None:
                currA = headB
            else:
                currA = currA.next

            if currB is None:
                currB = headA
            else:
                currB = currB.next
        return currA
