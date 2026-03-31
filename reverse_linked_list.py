from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    prev = None

    while current is not None:
        saved_next = current.next
        current.next = prev
        prev = current
        current = saved_next

    return prev

# Helpers
def to_list(node: Optional[ListNode]) -> list:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def to_linked_list(values: list) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


if __name__ == "__main__":
    assert to_list(reverse_list(to_linked_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(reverse_list(to_linked_list([1, 2]))) == [2, 1]
    assert to_list(reverse_list(to_linked_list([1]))) == [1]
    assert to_list(reverse_list(to_linked_list([]))) == []
    assert to_list(reverse_list(to_linked_list([1, 2, 3]))) == [3, 2, 1]
    print("All tests passed!")
