from .doubly_linked_list import LinkedList
from .helpers import Node

# Given two linked lists, where each linked list represents an integer, and each node
# in the linked list is digit of that integer, return a new linked list that
# represents the sum of integers represented by the two lists

# list one 2 -> 4 -> 7 -> 1
# list two 9 -> 4 -> 5

# 1742 + 549 = 2291


def sum_linked_lists(list_one, list_two):
    result = LinkedList()
    carry = 0

    list_one = list_one.head
    list_two = list_two.head

    while list_one or list_two:
        value_one = list_one.value if list_one else 0
        value_two = list_two.value if list_two else 0

        node_sum = value_one + value_two + carry

        carry = node_sum // 10  # floor div 18 // 10 -> 1; 9 // 10 -> 0

        node_sum = (
            node_sum % 10
        )  # modulus 18 % 10 -> 8; 9 % 10 -> 9 (0 quotient, rem 9)

        result.insert(Node(node_sum), insert_type="tail")

        list_one = list_one.next if list_one else None
        list_two = list_two.next if list_two else None

    if carry:
        result.insert(Node(carry), insert_type="tail")

    return result
