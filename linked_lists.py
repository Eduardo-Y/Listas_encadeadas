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


    def remove_first(self):
        if self.head == None:
            raise Exception('Lista Vazia!')

        self.head = self.head.next


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

    
    def remove_last(self):
        if self.head == None:
            raise Exception('Lista Vazia!')
        
        node = self.head
        while node is not None:
            if node.next.next == None:
                node.next = None
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
    

    def remove(self, target_node_data):
        if self.head == None:
            raise Exception('Lista Vazia!')
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        node = self.head
        while node is not None:
            if node.next.data == target_node_data:
                node.next = node.next.next
                return
            node = node.next
        raise Exception(f'"{target_node_data}" não foi encontrado!')
    

    def reverse(self):
        if self.head == None:
            raise Exception('Lista Vazia!')
        
        prev = None
        node = self.head
        while node is not None:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
            if node == None:
                self.head = prev


def main():
    first_node = Node('a')
    second_node = Node('b')
    third_node = Node('c')
    fourth_node = Node('d')
    linked_list = Linked_list()

    linked_list.add_first(first_node) # a -> None
    linked_list.add_last(fourth_node) # a -> d -> None
    linked_list.add_before(second_node, 'd') # a -> b -> d -> None
    linked_list.add_after(third_node, 'b') # a -> b -> c -> d -> None
    print(linked_list)
    linked_list.reverse() # d -> c -> b -> a -> None
    print(linked_list)
    linked_list.remove_first() # c -> b -> a -> None
    linked_list.remove_last() # c -> b -> None
    linked_list.remove('b') # c -> None
    linked_list.remove('c') # None
    print(linked_list)

if __name__ == "__main__":
    main()
