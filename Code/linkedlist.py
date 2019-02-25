#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        count = 0
        can_continue = True
        # checking if there's any items
        if self.head is not None:
            count += 1
            if self.head.next is not None:
                next = self.head.next
                while can_continue is True:
                    count += 1
                    if next.next is not None:
                        next = next.next
                    else:
                        can_continue = False
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(data=item)
        if self.head is not None:
            current_tail = self.tail
            if current_tail.next is None:
                current_tail.next = new_node
                self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(data=item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        # This one works...Probably not the way it's supposed to tho.
        can_continue = True
        if self.head is None:
            return False
        elif self.head.data is not quality:
            if self.head.next is not None:
                if self.head.next.data == quality:
                    return True
                next = self.head.next
                while can_continue is True:
                    if next.next is not None:
                        if next.next.data is not quality:
                            next = next.next
                        else:
                            return True
                            can_continue = False
                    else:
                        return False
            else:
                return False
        else:
            return True


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        can_continue = True
        if self.head is None:
            raise ValueError('List is empty: {}'.format(item))
        elif self.head.data is not item:
            if self.head.next is not None:
                next = self.head.next
                if next.data is item:
                    if next.next is not None:
                        self.head.next = next.next
                        self.tail = self.head.next
                    else:
                        self.head.next = None
                        self.tail = self.head
                    return
                while can_continue is True:
                    if next.next is not None:
                        if next.next.data is not item:
                            next = next.next
                        else:
                            if next.next.next is not None:
                                next.next = next.next.next
                            else:
                                print "deleting last item and setting new tail"
                                self.tail = next
                                next.next = None
                            can_continue = False
                    else:
                        raise ValueError('Item not found: {}'.format(item))
            else:
                raise ValueError('Item not found: {}'.format(item))
        else:
            if self.head.next is not None:
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))
        print('length: {}'.format(ll.length()))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))
            print('head: {}'.format(ll.head))
            print('tail: {}'.format(ll.tail))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

    # After implementing Prepend
    prepend_implemented = False
    if prepend_implemented:
        for item in ['3', '2', '1']:
            print('prepend({!r})'.format(item))
            ll.prepend(item)
            print('list: {}'.format(ll))
            print('length: {}'.format(ll.length()))

    # After implementing Find
    find_implemented = False
    if find_implemented:
        for item in ['A', '2', 'Z', 'B', '1', 'X']:
            print('find({!r})'.format(item))
            if ll.find(item):
                print('found: {!r}'.format(item))
            else:
                print('not found: {!r}'.format(item))

    # After implementing delete
    delete_implemented = False
    if delete_implemented:
        for item in ['B','C','A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            #     print('deleted: {!r}'.format(item))
            # else:
            #     print('could not delete: {!r}'.format(item))
            print('list: {}'.format(ll))
            print('tail: {}'.format(ll.tail))

if __name__ == '__main__':
    test_linked_list()
