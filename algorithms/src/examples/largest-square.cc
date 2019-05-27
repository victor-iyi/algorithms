/** Given a matrix containing 1s and 0s. Find the largest square made by 1s.
 *
 * @example
 *    INPUT:  1   1   0   1   0
 *            0   1   1   1   0
 *            1   1   1   1   0
 *            0   1   1   1   1
 *
 *    OUTPUT: 3
 *
 * @solution
 *   RECURSIVE SOLUTION:
 *
 *   ITERATIVE SOLUTION:
 *
 * @author
 *   Victor I. Afolabi
 *   Artificial Intelligence & Software Engineer.
 *   Email: javafolabi@gmail.com
 *   GitHub: https://github.com/victor-iyiola
 *
 * @project
 *   File: largest-square.cc
 *   Created on 26 August, 2018 @ 4:26 PM.
 *
 * @license
 *   MIT License
 *   Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
 **/
#include <algorithm>
#include <vector>

size_t largestSquare(const std::vector<std::vector<size_t> >& matrix) {
  // Clone the matrix (cache) for computing neighbors.
  std::vector<std::vector<size_t> > cache = matrix;

  size_t result = 0, row, col;

  // for (row = 0; row < matrix.size(); row++) {
  //   for (col = 0; col < matrix[0].size(); col++) {
  //     if (row == 0 || col == 0)
  //       continue;  // Edges remain the same. No updates needed.
  //     else if (matrix[row][col] > 0)
  //       // Update based on neighbors.
  //       // Update Rule: `min(neighbors) + self`
  //       cache[row][col] += std::min(cache[row][col - 1], cache[row - 1][col],
  //                                   cache[row - 1][col - 1]);

  //     // Update result.
  //     if (cache[row][col] > result) cache[row][col] = result;

  //   }  // end col.
  // }    // end row.

  return result;
}
