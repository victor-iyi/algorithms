#ifndef _ALGORITHMS_H
#define _ALGORITHMS_H

#include <vector>

namespace algo {

// Invalid position (couldn't find element).
static const size_t npos = -1;

// Binary search algorithm.
// template <typename T>
size_t binarySearch(const std::vector<int>&, const int&);

// Recursive binary search algorithm.
template <typename T>
size_t binarySearch(const std::vector<T>&, const T&, const size_t& left, const size_t& right);

template <typename T>
size_t breadthFirstSearch(const std::vector<T>&, T);

template <typename T>
size_t depthFirstSearch(const std::vector<T>&, T);

};  // namespace algo

#endif  //_ALGORITHMS_H
