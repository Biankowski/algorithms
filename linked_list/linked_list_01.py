# É muito mais fácil inserir um dado em uma lista encadeada do que em um array, simplesmente pela forma na qual ela é organizada na memória.
# Um array é organizado em forma sequencial com um espaço pré definido. Para inserir um dado em um array é necessário criar um novo array em outro espaço de memória,
# e copiar o array antigo para ele. Esse processo se torna lento em grandes datasets.

# Listas encadeadas são organizadas em memória por meio de nodes e ponteiros. Cada node contém um número e um ponteiro apontando para o próximo elemento dessa lista.
# Dessa forma, a operação de inserção de um número no meio da lista se torna muito mais simples e rápida.
# Basta reordenar os ponteiros de cada node.
# A complexidade de tempo para inserir ou deletar um elementos em uma lista encadeada é de tempo constante O(1).

# A desvantagem das listas encadeadas é que não é possível indexar os elementos dela com valores tipo lista[0], lista[1], etc.
# Isso torna o processo de busca mais lento do que eu um array. A complexidade de busca em uma lista encadeada será de O(n), e em um array será tempo constante O(1).
