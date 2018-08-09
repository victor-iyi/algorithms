#include "../include/algorithms.h"
#include <vector>

// Sorting algorithms.
namespace sort {

/** Binary sort algorithm.
 *
 * @details:
 *  Complexity:
 *    Worst Case:   O(nlogn)
 *    Average Case: O(logn)
 *    Best Case:    O(logn)
 *
 * @params
 *  const std::vector<T>& vec - Unsorted values.
 *
 * @returns
 *  std::vector - Sotred values.
 */
template <typename T>
std::vector<T> binary(const std::vector<T>& vec) {
  return vec;
}

};  // namespace sort

// Search algorithms.
namespace search {

/** Binary search algorithm. (Iterative method).
 *
 * @details:
 *  Complexity:
 *    Worst Case:   O(nlogn)
 *    Average Case: O(logn)
 *    Best Case:    O(logn)
 *
 * @params
 *  const std::vector<T>& values - Sorted list of values.
 *  const T& item - Item to look search in `values`.
 *
 * @returns
 *  bool - Whether or not the `item` is contained in the list of `values`.
 */
template <typename T>
bool binary(const std::vector<T>& values, const T& item) {
  size_t left = 0;
  size_t right = values.size();
  // size_t mid = (right + left) / 2;
  size_t mid = left + ((right - left) / 2);

  // Iterative method.
  while (left <= right) {
    if (values[mid] == item) {
      return true;
    } else if (item < values[mid]) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return false;
}

/** Binary search algorithm. (Recursive method).
 *
 * @details:
 *  Complexity:
 *    Worst Case:   O(nlogn)
 *    Average Case: O(logn)
 *    Best Case:    O(logn)
 *
 * @params
 *  const std::vector<T>& values - Sorted list of values.
 *  const T& item - Item to look search in `values`.
 *  const size_t left - Index of element to the left of mid-point.
 *  const size_t right - Index of element to the right of mid-point.
 *
 * @returns
 *  bool - Whether or not the `item` is contained in the list of `values`.
 */
template <typename T>
bool binary(const std::vector<T>& values, const T& item, size_t left,
            size_t right) {
  if (left > right) return false;

  // int mid = (left + right) / 2;
  int mid = left + ((right - left) / 2);
  if (values[mid] == item)
    return true;
  else if (values[mid] < left)
    return search::binary(values, item, left, mid - 1);
  else
    return search::binary(values, item, mid + 1, right);

  return false;
}

};  // namespace search
