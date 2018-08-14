#include "../../include/Core/Algorithms.h"
#include <iostream>

/**
 * Binary search iterative implementation.
 *
 * Complexity:
 *    Average:  O(logn)
 *    Worst:    O(n)
 */
// template <typename T>
size_t algo::binarySearch(const std::vector<int>& values, const int& item) {
  // Lower & upper bounds.
  size_t lower = 0, upper = values.size() - 1;

  // Mid point.
  size_t middle = (upper + lower) / 2;

  do {
    if (values[middle] == item)
      return middle;
    else if (values[middle] < item)
      upper = middle - 1;
    else
      lower = middle + 1;

    middle = (upper + lower) / 2;  // recalculate the mid point.
  } while (lower <= upper);

  // Item was not found.
  return algo::npos;
}

/** Binary Search Recursive implementation.
 *
 * Complexity:
 *    Average: O(logn)
 *    Worst: O(n)
 */
template <typename T>
size_t binarySearch(std::vector<T>& data, const T& value, const size_t& left,
                    const size_t& right) {
  // If the left & right crosses each other.
  if (left >= right) return algo::npos;

  // Calculate midpoint.
  size_t middle = (right + left) / 2;

  if (data[middle] == value)
    return middle;
  else if (data[middle] < value)
    return algo::binarySearch(data, value, left, middle - 1);
  else
    return algo::binarySearch(data, value, middle + 1, right);
}

template <typename T>
size_t algo::breadthFirstSearch(const std::vector<T>& graph, T item) {
  return algo::npos;
}

template <typename T>
size_t algo::depthFirstSearch(const std::vector<T>& graph, T item) {
  return algo::npos;
}
