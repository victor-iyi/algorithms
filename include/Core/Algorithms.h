#ifndef _ALGORITHMS_H
#define _ALGORITHMS_H

#include <vector>

namespace algo {

// Invalid position (couldn't find element).
static const size_t npos = -1;

/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Search Algorithms.
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */
namespace search {
// Iterative binary search algorithm.
// template <typename T>
size_t binarySearch(const std::vector<int>&, const int&);
void displayBinarySearch(const std::vector<int>&);
void displayBinarySearch(const std::vector<int>&, const int&, const int&);

// Recursive binary search algorithm.
template <typename T>
size_t binarySearch(const std::vector<T>&, const T&, const size_t& left,
                    const size_t& right);

template <typename T>
size_t breadthFirstSearch(const std::vector<T>&, const T&);

template <typename T>
size_t depthFirstSearch(const std::vector<T>&, const T&);

};  // namespace search

/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Sorting Algorithms.
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */
namespace sort {

/* Bubble Sort. O(n^2) */
template <typename T>
void bubble(std::vector<T>&);

/* Merge Sort O(logn) */ 
template <typename T>
void merge(std::vector<T>&);

/* Quick Sort */ 
template <typename T>
void quick(std::vector<T>&);

/* Insertion Sort */ 
template <typename T>
void insertion(std::vector<T>&);

};  // namespace sort

/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Algorithmic Checks.
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */
namespace check {
/* Palindrome */
template <typename T, size_t Size>
bool isPalindrome(const T&);

/* Prime Number. */
bool isPrimeNumber(const int&);

/* Perfect Number. */
bool isPerfectNumber(const int&);

/* Armstrong Number. */
bool isArmstrong(const int&);

};  // namespace check

};  // namespace algo

#endif  //_ALGORITHMS_H
