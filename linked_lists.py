class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class Linked_list:
    def __init__(self):
        self.head = None


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def add_first(self, new_node):
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node


    def add_last(self, new_node):
        if self.head == None:
            self.head = new_node
            return

        node = self.head
        while node != None:
            if node.next == None:
                node.next = new_node
                return
            node = node.next


    def add_before(self, new_node, target_node_data):
        if self.head == None:
            raise Exception('Lista Vazia!')
        
        node = self.head
        while node is not None:
            if node.next.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
            node = node.next
        raise Exception(f'"{target_node_data}" não foi encontrado!')

    def add_after(self, new_node, target_node_data):
        if self.head == None:
            raise Exception('Lista Vazia!')

        node = self.head
        while node is not None:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
            node = node.next
        raise Exception(f'"{target_node_data}" não foi encontrado!')

first_node = Node('a')
second_node = Node('b')
third_node = Node('c')
fourth_node = Node('d')
linked_list = Linked_list()

linked_list.add_first(first_node)
linked_list.add_last(fourth_node)
linked_list.add_before(second_node, 'd')
linked_list.add_after(third_node, 'b')
print(linked_list)