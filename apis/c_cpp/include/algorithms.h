#ifndef _ALGORITHMS_H
#define _ALGORITHMS_H

#include <vector>

// For sorting algorithms.
namespace sort {

// Binary search.
template <typename T>
std::vector<T> binary(const std::vector<T>&);
};  // namespace sort

// For search algorithms.
namespace search {

// Binary search (Iterative method).
template <typename T>
bool binary(const std::vector<T>&, const T&);

// Binary search (Recursive method).
template <typename T>
bool binary(const std::vector<T>&, const T&, size_t left, size_t right);
};  // namespace search

#endif /* defined(_ALGORITHMS_H) */
