#include "../../include/Core/Algorithms.h"
#include <iostream>

// template <typename T>
bool algo::binarySearch(const std::vector<int>& values, const int& item) {
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
