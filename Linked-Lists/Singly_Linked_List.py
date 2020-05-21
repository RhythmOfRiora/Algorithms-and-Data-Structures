

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def retrieve_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node



class Singly_Linked_List(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def find_size(self):
        current = self.head
        size = 0
        while current.get_next:
            size += 1
            current = current.get_next()
        return size

    def search(self, value):
        current = self.head
        while current.get_next():
            if current.data == value:
                return current
            else:
                current = current.get_next()
        raise ValueError("Item is not in list.")

    def delete(self, value):
        current = self.head
        last_node = self.head
        while current.get_next():
            if current.data == value:
                last_node.set_next(current.get_next())
            else:
                last_node = current
                current = current.get_next()
        raise ValueError("Item is not in list.")
