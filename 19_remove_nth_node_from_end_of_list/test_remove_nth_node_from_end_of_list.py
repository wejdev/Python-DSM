import pytest
from remove_nth_node_from_end_of_list import remove_nth_node_from_end_of_list, ListNode

test_cases = [
    ([], 0, []),
    ([1], 1, []),
    ([1, 2], 1, [1]),
    ([1, 2], 2, [2]),
    ([1, 2, 3], 1, [1, 2]),
    ([1, 2, 3], 2, [1, 3]),
    ([1, 2, 3], 3, [2, 3]),
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 6, 7, 8, 9]),
]

def list_to_array(node):
    array = []
    while node:
        array.append(node.val)
        node = node.next
    return array

def array_to_list(nums):
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

@pytest.mark.parametrize("head, n, expected", test_cases)
def test_remove_nth_node_from_end_of_list(head, n, expected):
    head_node = array_to_list(head)
    new_head = remove_nth_node_from_end_of_list(head_node, n)
    assert list_to_array(new_head) == expected
