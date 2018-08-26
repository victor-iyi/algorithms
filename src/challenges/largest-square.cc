/** Given an array which contains indices to the same array,
 *  find if the given array has a cycle or not.
 *
 * @solution
 *   The classic Rabbit and Turtle technique is used to solve this
 *   problem. For every two steps that the Rabbit (P) takes, the
 *   Turtle (Q) takes one.
 *   A cycle is found if P == Q or if the array goes out of bounds.
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
  std::vector<std::vector<size_t> > cache = matrix;
  size_t result = 0, row, col;

  for (row = 0; row < matrix.size(); row++) {
    for (col = 0; col < matrix[0].size(); col++) {
      if (row == 0 || col == 0) {
      } else if (matrix[row][col] > 0) {
        cache[row][col] = 1 + std::min(cache[row][col - 1], cache[row - 1][col],
                                       cache[row - 1][col - 1]);
      }  // end else if.

      // Update result.
      if (cache[row][col] > result) cache[row][col] = result;

    }  // end col.
  }    // end row.

  return result;
}
