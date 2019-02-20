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
        if self.head.next is not None:
            count += 1
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
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
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

        if self.head is not None:
            if self.head.data is item:
                if self.head.next is not None:
                    self.head = self.head.next
                else:
                    self.head = None
            else:
                """ If the item is not the Head but it has a head"""
                if self.head.next is not None:
                    next_item = self.head.next
                    if next_item is item:
                        if self.head.next.next is not None:
                            self.head.next = self.head.next.next
                        else:
                            self.head.next = None
                    else:
                        """ If it's not either the first or second item """
                        found = False
                        while found is False:
                            if next_item.next == item:
                                if next_item.next.next is not None:
                                    next_item.next = next_item.next.next
                                else:
                                    next_item.next = None
                                found = True
                                break
                            else:
                                if next_item.next is not None:
                                    next_item = next_item.next
                                else:
                                    ValueError('Item not found: {}'.format(item))
                                    break
        else:
            print "stops at the beginning"
            ValueError('Item not found: {}'.format(item))

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

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
    delete_implemented = True
    if delete_implemented:
        for item in ['A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            #     print('deleted: {!r}'.format(item))
            # else:
            #     print('could not delete: {!r}'.format(item))
            print('list: {}'.format(ll))

if __name__ == '__main__':
    test_linked_list()
