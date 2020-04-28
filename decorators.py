from timeit import default_timer as timer

def time_func (*args,**kwargs):
    def __time(func):
        nonlocal args, kwargs
        t0 = timer()
        func(*args, **kwargs)
        elapsed_time = (timer() - t0) * 1000
        print('Called function', func.__name__)
        print(f'Execution time: {elapsed_time:.3g} ms')

        return elapsed_time

    return __time

# Exercício 10
@time_func()
def test ():
    for i in range(100):
        print(i+1, end = '\t')
    print()

print()

# Exercício 11
timer1 = time_func ('Testing', 'args', 'list\n', end = 'Testing args dict\n')
time(print)
