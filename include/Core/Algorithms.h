#ifndef _ALGORITHMS_H
#define _ALGORITHMS_H

#include <string>
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

// template <typename T>
size_t binarySearch(const std::vector<int>&, const int&, const size_t& left,
                    const size_t& right);

// Recursive binary search algorithm.

template <typename T>
size_t breadthFirstSearch(const std::vector<T>&, const T&);

template <typename T>
size_t depthFirstSearch(const std::vector<T>&, const T&);

};  // namespace search

/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Display.
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */
namespace display {
void binarySearch(const std::vector<int>&);
void binarySearch(const std::vector<int>&, const int&, const int&);

};  // namespace display
/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Sorting Algorithms.
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */
namespace sort {

/* Bubble Sort. O(n^2) */
// template <typename T>
void bubble(std::vector<int>&);

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
namespace is {
/* Palindrome */
template <typename T, size_t Size>
bool palindrome(const T&);

/* Anagram. */
bool anagram(const std::string&);

/* Prime Number. */
bool primeNumber(const int&);

/* Perfect Number. */
bool perfectNumber(const int&);

/* Armstrong Number. */
bool armstrong(const int&);
bool armstrong(const std::string&);

};  // namespace is

};  // namespace algo

#endif  //_ALGORITHMS_H
