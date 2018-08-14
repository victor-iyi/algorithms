#ifndef _ALGORITHMS_H
#define _ALGORITHMS_H

#include <vector>

namespace algo {

// Binary search algorithm.
// template <typename T>
bool binarySearch(const std::vector<int>&, const int&);

// Recursive binary search algorithm.
template <typename T>
bool binarySearch(std::vector<T>&, T&, size_t left, size_t right);

template <typename T>
bool breadthFirstSearch(const std::vector<T>&, T);

template <typename T>
bool depthFirstSearch(const std::vector<T>&, T);

};  // namespace algo

#endif  //_ALGORITHMS_H
