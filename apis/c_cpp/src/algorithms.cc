#include "../include/algorithms.h"
#include <vector>

// Sorting algorithms.
namespace sort {

/** Binary search algorithm.
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
namespace search {};
