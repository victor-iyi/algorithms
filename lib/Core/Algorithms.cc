#include <iostream>
#include "Core/Algorithms.h"

// template <typename T>
bool algo::binarySearch(const std::vector<int>& values, int item) {
  std::cout << "Searching for \"" << item << "\" in: ";
  for (int val : values)
    std::cout << val << ' ';

  return false;
}
