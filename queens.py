# Exercício 4

# Obs.: O problema pode ser resolvido com um tempo médio menor que 1 minuto
#       quando o tamanho do tabuleiro é menor que 17x17

def share_diagonal (x0,y0,x1,y1):
    dy = y1 - y0
    dx = x1 - x0
    return dy*dy == dx*dx # Avoid abs() call and floating point error

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
        with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def main():
    import random
    import sys
    from timeit import default_timer as timer
    rng = random.Random()   # Instantiate a generator

    try:
        n = int(sys.argv[1])
    except (ValueError,IndexError):
        n = 8

    bd = list(range(n))     # Generate the initial permutation
    num_found = 0
    tries = 0

    times = []

    t0 = timer()

    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            t1 = timer()
            dt = t1 - t0
            t0 = t1
            times.append(dt)
            print("Found solution {0} in {1} tries and {2:.2g} seconds.".format(bd, tries, dt))
            tries = 0
            num_found += 1

    print('Mean time: {:.2g} seconds'.format(sum(times)/10))

if __name__ == '__main__':
    main()
