class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Индекс вне диапазона")
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node.data

    def __str__(self):
        current_node = self.head
        linked_list_str = ''
        while current_node:
            linked_list_str += f'{current_node.data} -> '
            current_node = current_node.next
        linked_list_str += 'None'
        return linked_list_str