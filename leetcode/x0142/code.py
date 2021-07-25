# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self) -> str:
        return f"{ListNode(self.val, self.next)}"

    def __str__(self) -> str:
        return self.__repr__()


def detectCycle(head: ListNode) -> ListNode:
    """
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.
    """
    fast, slow = head, None
    while (fast is not slow):
        if slow is None:
            slow = head
        if fast is None or fast.next is None:
            # fast is at end, no cycle
            return None
        else:
            fast = fast.next.next
            slow = slow.next
    
    # here means fast meet slow, and we know there is a cycle
    fast = head 
    while (fast is not slow):
        slow = slow.next
        fast = fast.next
    
    return fast
    
