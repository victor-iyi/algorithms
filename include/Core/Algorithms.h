#ifndef _ALGORITHMS_H
#define _ALGORITHMS_H

#include <vector>

namespace algo {

// Binary search algorithm.
// template <typename T>
bool binarySearch(const std::vector<int>&, int);

// Recursive binary search algorithm.
template <typename T>
bool binarySearchRecurse(std::vector<T>&, T&, size_t left, size_t right);

};  // namespace algo

#endif  //_ALGORITHMS_H
