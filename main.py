from algorithms.cython import algorithms


def main():
    no = int(input('Enter a number: '))

    fib = algorithms.fibonacci(no)
    fac = algorithms.factorial(no)

    print('fibonacci({}) = {}'.format(no, fib))
    print('factorial({}) = {}'.format(no, fac))


if __name__ == '__main__':
    main()
