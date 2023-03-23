# A estrutura de dados de uma árvore binária é organizada de tal forma que existe um elemento central "root", e existem duas possibilidades de alocação dos outros elementos.
# Os elementos podem ser alocados para a direita ou para a esquerda.
# O que determina se um elemento será alocado para direita ou para a esquerda é o tamando dele em relação ao node em questão.
# Caso o elemento seja menor que o elemento do determinado node, esse elemento será alocado à esquerda do node; caso seja maior, será alocado à direita do node.

# O algoritimo de alrvore binária usa recursão.

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)


root = Node('g')

root.insert('c')
root.insert('b')
root.insert('a')
root.insert('e')
root.insert('d')
root.insert('f')
root.insert('i')
root.insert('h')
root.insert('j')
root.insert('k')
