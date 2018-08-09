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

/** Binary search algorithm.
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

  // Recursive method.
}
};  // namespace search
