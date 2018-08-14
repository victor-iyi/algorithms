#ifndef _ALGORITHMS_H
#define _ALGORITHMS_H

#include <vector>

namespace algo {

// Invalid position (couldn't find element).
static const size_t npos = -1;

// Iterative binary search algorithm.
// template <typename T>
size_t binarySearch(const std::vector<int>&, const int&);

// Recursive binary search algorithm.
template <typename T>
size_t binarySearch(const std::vector<T>&, const T&, const size_t& left,
                    const size_t& right);

template <typename T>
size_t breadthFirstSearch(const std::vector<T>&, const T&);

template <typename T>
size_t depthFirstSearch(const std::vector<T>&, const T&);

template <typename T, size_t Size>
bool isPalindrome(const T&);

bool isPrimeNumber(const int&);
bool isPerfectNumber(const int&);
bool isArmstrong(const int&);

};  // namespace algo

#endif  //_ALGORITHMS_H
