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

    def add_node_after(self, new_node, index_node):
        if self.head == None:
            return 'Lista Vazia'

        node = self.head
        while node != None:
            if node.data == index_node:
                new_node.next = node.next
                node.next = new_node
                return f'"{new_node.data}" foi adicionado com sucesso!'
            node = node.next
        return 'Valor não encontrado na lista!'

fist_node = Node('a')
secund_node = Node('b')
tirth_node = Node('c')

linked_list = Linked_list()
linked_list.head = fist_node
print(linked_list.add_node_after(tirth_node, 'a'))
print(linked_list)