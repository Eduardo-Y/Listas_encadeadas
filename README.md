## Implentação de Listas Encadeadas com Python

Este repositório contém uma implementação simples de uma **Lista Encadeada** (Linked List) em Python. A lista encadeada é uma estrutura de dados linear, onde os elementos não são armazenados em locais de memória contíguos. Em vez disso, cada elemento (nó) contém o dado e uma referência (ponteiro) para o próximo nó na sequência.

### Estrutura do Código

O código é composto por duas classes principais:

- **`Node`**: Representa um nó individual na lista encadeada. Cada nó possui:

  - `data`: O valor armazenado no nó.
  - `next`: Uma referência para o próximo nó na lista. Se for o último nó, `next` é `None`.
  - O método `__repr__` permite uma representação string simples do dado contido no nó.

- **`Linked_list`**: Representa a lista encadeada propriamente dita. Ela possui:
  - `head`: Uma referência para o primeiro nó da lista. Se a lista estiver vazia, `head` é `None`.
  - O método `__repr__` fornece uma representação string da lista, mostrando os dados de cada nó conectados por " -> " e terminando com "None".
  - O método `__iter__` permite iterar sobre os nós da lista, tornando possível usar a lista em loops `for`.
  - `add_first(new_node)`: Adiciona um novo nó no início da lista.
  - `remove_first()`: Remove o primeiro nó da lista. Levanta uma exceção se a lista estiver vazia.
  - `add_last(new_node)`: Adiciona um novo nó no final da lista.
  - `remove_last()`: Remove o último nó da lista. Levanta uma exceção se a lista estiver vazia.
  - `add_before(new_node, target_node_data)`: Adiciona um novo nó antes do primeiro nó que contém o `target_node_data`. Levanta uma exceção se a lista estiver vazia ou se o `target_node_data` não for encontrado.
  - `add_after(new_node, target_node_data)`: Adiciona um novo nó depois do primeiro nó que contém o `target_node_data`. Levanta uma exceção se a lista estiver vazia ou se o `target_node_data` não for encontrado.
  - `remove(target_node_data)`: Remove o primeiro nó que contém o `target_node_data`. Levanta uma exceção se a lista estiver vazia ou se o `target_node_data` não for encontrado.
  - `reverse()`: Inverte a ordem dos nós na lista encadeada. Levanta uma exceção se a lista estiver vazia.

### Como Usar

Para utilizar a implementação da lista encadeada, você pode importar as classes `Node` e `Linked_list` em seu código Python:

```python
from your_module import Node, Linked_list

# Criando nós
node_a = Node('apple')
node_b = Node('banana')
node_c = Node('cherry')

# Criando uma lista encadeada
my_list = Linked_list()

# Adicionando nós
my_list.add_first(node_a)
my_list.add_last(node_c)
my_list.add_before(node_b, 'cherry')

# Imprimindo a lista
print(my_list)  # Saída: apple -> banana -> cherry -> None

# Iterando sobre a lista
for node in my_list:
    print(node.data)

# Removendo elementos
my_list.remove_last()
print(my_list)  # Saída: apple -> banana -> None

# Revertendo a lista
my_list.reverse()
print(my_list)  # Saída: banana -> apple -> None
```

O arquivo `main()` no código de exemplo demonstra algumas das operações básicas da lista encadeada.

### Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues para relatar bugs ou sugerir melhorias, ou enviar pull requests com suas modificações.

Código escrito com ajuda do artigo sobre listas encadeadas do site "Real Python" que encontra-se no seguinte link: https://realpython.com/linked-lists-python/#implementing-your-own-linked-list
