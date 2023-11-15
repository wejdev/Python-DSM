class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_nth_node_from_end_of_list(first_node, nodes_from_end):
    if first_node is None:
        return first_node

    head = ListNode(0)
    head.next = first_node

    lagging_node = head
    seeking_node = head

    for i in range(nodes_from_end + 1):
        seeking_node = seeking_node.next

    while seeking_node:
        lagging_node = lagging_node.next
        seeking_node = seeking_node.next

    deleted_node = lagging_node.next
    lagging_node.next = deleted_node.next

    return head.next


"""*
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 """

"""
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
"""
