# medium, linked list
# https://www.hackerrank.com/challenges/one-week-preparation-kit-merge-two-sorted-linked-lists/problem
# (class and methods available on hackerrank)

def mergeLists(head1, head2):
    llist = SinglyLinkedList()

    while head1 and head2:
        if head1.data > head2.data:
            llist.insert_node(head2.data)
            head2 = head2.next
        else:
            llist.insert_node(head1.data)
            head1 = head1.next
    while head1:
        llist.insert_node(head1.data)
        head1 = head1.next
    while head2:
        llist.insert_node(head2.data)
        head2 = head2.next

    return llist.head
