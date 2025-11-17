class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_end(head, data):
    new_node = Node(data)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

def safe_print(head):
    print("Linked List:", end=" ")
    curr = head.next  # skip dummy
    while curr:
        print(curr.data, end=" → ")
        curr = curr.next
    print("None")

def find_middle(head):
    if not head:
        return head
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    dummy = Node("")
    temp = dummy
    while left and right:
        if left.data <= right.data:
            temp.next = left
            left = left.next
        else:
            temp.next = right
            right = right.next
        temp = temp.next
    temp.next = left if left else right
    return dummy.next

def merge_sort(head):
    if not head or not head.next:
        return head
    
    mid = find_middle(head)
    second_head = mid.next
    mid.next = None
    left = merge_sort(head)
    right = merge_sort(second_head)

    return merge(left, right)
# Test
def main():
    head = Node("")  # dummy
    insert_end(head, 1)
    insert_end(head, 5)
    insert_end(head, 4)
    insert_end(head, 8)
    insert_end(head, 2)
    insert_end(head, 9)
    insert_end(head, 7)
    insert_end(head, 6)
    safe_print(head)
    head.next = merge_sort(head.next)
    print("List after sorting")
    safe_print(head)
main()

## output ##
# Linked List: 1 → 5 → 4 → 8 → 2 → 9 → 7 → 6 → None
# List after sorting
# Linked List: 1 → 2 → 4 → 5 → 6 → 7 → 8 → 9 → None
