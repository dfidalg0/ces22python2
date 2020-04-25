# Exercício 8

from timeit import default_timer as timer

def time_func (func):
    t0 = timer()
    func()
    print('Called function', func.__name__)
    print('Execution time:',(timer() - t0) * 1000, 'ms')

@time_func
def test ():
    for i in range(1000):
        print(i+1, end = '\t')
    print()
