#include "../../include/Core/Algorithms.h"
#include <iostream>

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

  std::cout << "Searching for \"" << item << "\" in: ";
  for (const int& val : values) std::cout << val << ' ';

  return false;
}

template <typename T>
bool algo::breadthFirstSearch(const std::vector<T>& graph, T item) {
  return false;
}

template <typename T>
bool algo::depthFirstSearch(const std::vector<T>& graph, T item) {
  return false;
}
