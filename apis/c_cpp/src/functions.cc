#include "functions.h"


/**
 * Find the nth fibonacci number.
 *
 * @param n
 *    The nth term.
 *
 * @return int
 *    The nth fibonacci number.
 */
int fibonacci(int n)
{
  // Local variables.
  int a = 0, b = 1, temp;
  for (int i = 0; i < n; i++)
  {
    temp = a;
    a = a + b;
    b = temp;
  }

  return a;
}

/**
 * Find the factorial of a given number.
 *
 * @param n
 *    The nth term.
 *
 * @return int
 *    Computed factorial of n.
 */
int factorial(int n)
{

  // Base case.
  if (n < 2)
    return n;

  // Recursive call.
  return factorial(n - 1);
}
