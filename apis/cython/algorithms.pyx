

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Calculate the nth Fibonacci number.
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
def fibonacci(int n):
  """Finds the nth fibonacci number.

  :params:
    n: int
      The nth term to be computed.

  :returns:
    int, factorial(n)
    Returns the nth fibonacii number.
  """
  cdef int a = 0, b = 1
  cdef int i = 0

  for i in range(n):
    a, b = a + b, a
    i += 1

  return a



################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Calculate the nth factorial.
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
def factorial(int n):
  """Calculates the factorial of a given number.

  === Parameters ===
  n: int
    The n'th number to be computed.

  === Returns ===
  int, factorial(n)
    The computed factorial of `n`.
  """
  return n if n < 2 else factorial(n-1)
