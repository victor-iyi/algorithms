

###############################################################
# +———————————————————————————————————————————————————+
# | Calculate the nth Fibonacci number.
# +———————————————————————————————————————————————————+
###############################################################
cpdef fibonacci(int n):
  """Finds the nth fibonacci number.

  Args:
    n (int): The nth term to be computed.

  Returns:
    int: Returns the nth fibonacci number.
  """
  cdef int a = 0, b = 1, i = 0

  for i in range(n):
    a, b = a + b, a
    i += 1

  return a



###############################################################
# +———————————————————————————————————————————————————+
# | Calculate the nth factorial.
# +———————————————————————————————————————————————————+
###############################################################
cpdef factorial(int n):
  """Calculates the factorial of a given number.

  Args:
    n (int): The n'th number to be computed.

  Returns:
    int: The computed factorial of `n`.
  """
  return n if n < 2 else factorial(n-1)
