# Exercício 12

from point import Point

L1 = list(range(1,10 + 1))

L2 = [i * Point(i,11-i) for i in range(1,10 + 1)]

# A função print para lista chama a função __repr__ para cada elemento
# Como __repr__ está implementada tanto para as classes <'int'> e <'point.Point'>
# as duas chamadas imprimem os objetos no formato desejado
print(L1)
print(L2)

# Como a operação de soma está implementada tanto para as classes <'int'> e
# <'point.Point'>, as duas chamadas de sum funcionam normalmente
print(sum(L1))
print(sum(L2))
