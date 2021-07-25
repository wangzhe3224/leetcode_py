from typing import List
from leetcode.x0142.code import ListNode, detectCycle


def test_sol():

    list_nodes = [
        ListNode(i)
        for i in range(10)
    ]

    head_no_cycle = ListNode(
        x=1,
        next=ListNode(x=2, next=None)
    )

    # 0 -> 1 -> 2 -> 1
    head_cycle = list_nodes[0]
    head_cycle.next = list_nodes[1]
    head_cycle.next.next = list_nodes[2]
    head_cycle.next.next.next = list_nodes[1]
    
    params = [
        ( head_no_cycle, None ),
        ( head_cycle, list_nodes[1] ),
    ]

    for args, exp in params:
        res = detectCycle(args)
        assert res is exp