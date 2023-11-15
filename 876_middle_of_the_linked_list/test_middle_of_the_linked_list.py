import pytest
from middle_of_the_linked_list import ListNode, middle_node

def list_from_array(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def array_from_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

@pytest.mark.parametrize("head, expected", [
    ([0], [0]),
    ([6], [6]),
    ([0, 1], [1]),
    ([1, 2, 3], [2, 3]),
    ([0, 1], [1]),
    ([1, 0], [0]),
    ([1, 0, 2, 0, 3, 0, 4], [0, 3, 0, 4]),
    ([1, 0, -2, 6, 3, 0, 5, 4, 0], [3, 0, 5, 4, 0]),
    ([1, 0, -2, 6, 3, 7, 5, 4, 0, 8], [7, 5, 4, 0, 8]),
    ([1, 2, 3, 4, 5], [3, 4, 5]),
    ([1, 2, 3, 4, 5, 6], [4, 5, 6])
])
def test_middle_of_the_linked_list(head, expected):
    linked_list = list_from_array(head)
    middle_nodes = middle_node(linked_list)
    assert array_from_list(middle_nodes) == expected
