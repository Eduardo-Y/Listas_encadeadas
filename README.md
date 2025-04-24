Aqui está o README gerado para o código que você forneceu:

---

# Linked List Implementation in Python

Este repositório contém uma implementação de uma lista encadeada em Python. A lista encadeada é uma estrutura de dados linear composta de "nós", onde cada nó contém um valor (`data`) e uma referência (`next`) ao próximo nó na sequência.

## Estrutura do Código

### Classe Node
A classe `Node` representa um único elemento na lista encadeada. Cada nó contém:
- `data`: O valor armazenado no nó.
- `next`: Referência ao próximo nó na lista (inicialmente `None`).

#### Métodos:
- `__init__(self, data)`: Inicializa o nó com um valor.
- `__repr__(self)`: Retorna uma representação em string do valor do nó.

### Classe Linked_list
A classe `Linked_list` gerencia a lista encadeada. Ela contém:
- `head`: Referência para o primeiro nó da lista (inicialmente `None`).

#### Métodos:
- `__init__(self)`: Inicializa uma lista encadeada vazia.
- `__repr__(self)`: Retorna uma representação em string da lista encadeada, mostrando a sequência de nós.
- `__iter__(self)`: Permite iterar pelos nós da lista encadeada.
- `add_first(new_node)`: Adiciona um novo nó no início da lista.
- `add_last(new_node)`: Adiciona um novo nó no final da lista.
- `add_before(new_node, target_node_data)`: Adiciona um novo nó antes de um nó-alvo especificado.
- `add_after(new_node, target_node_data)`: Adiciona um novo nó após um nó-alvo especificado.

## Exemplo de Uso
O código abaixo demonstra como usar as classes `Node` e `Linked_list`:

```python
first_node = Node('a')
second_node = Node('b')
third_node = Node('c')
fourth_node = Node('d')
linked_list = Linked_list()

linked_list.add_first(first_node)
linked_list.add_last(fourth_node)
linked_list.add_before(second_node, 'd')
linked_list.add_after(third_node, 'b')
print(linked_list)  # Saída: a -> b -> c -> d -> None
```

## Recursos Adicionais
- **Manipulação Dinâmica**: Você pode adicionar novos nós em qualquer posição na lista encadeada.
- **Iteração**: A lista encadeada suporta iteração fácil usando o método `__iter__`.

---

Se precisar de ajustes ou preferir incluir algo mais, é só dizer! 😊