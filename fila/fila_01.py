# A estrutura de dados Fila funciona literalmente como uma fila.
# É um estrutura de dados conhecida como FIFO (First in, first out). Ou seja, o primeiro elemento adicionado na fila será o primeiro a sair.
# Podemos imaginar como se fosse um fila de um banco. A primeira pessoa na fila será a primeira a ser atendida, em seguida a segunda, e assim por diante...

# Adicionar um elemento na fila é chamado de 'enqueue'(add)(offer).
# Remover um elemento da fila é chamado de 'dequeue'(remove)(poll).

# O primeiro elemento da fila é chamado de Head, enquanto o último elemento da fila é chamado de Tail.
# Toda vez que um elemento é removido da fila, o Head passa para o elemento seguinte.
# Toda vez que um elemento é adicionado a fila, esse elemento passa a ser o Tail.
# Caso tenha somente um elemento na fila, esse elemento será tanto o Head, quanto o Tail.

# A fila é útil em vários cenários, por exemplo:
# Keyboard buffer.
# Printer queue.
# Linked Lists, Priority Queue, Breadth-first-search.
