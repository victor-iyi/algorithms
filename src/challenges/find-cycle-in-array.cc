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
 *   File: find-cycle-in-array.cc
 *   Created on 26 August, 2018 @ 10:15 AM.
 *
 * @license
 *   MIT License
 *   Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
 **/

#include <vector>

/** Find if an array has a cycle or not.
 *
 * @params
 *  arr std::vector<int>: Array which contains indices to itself.
 *
 * @return
 *  bool -- true if a cycle is detected, false otherwise.
 */
bool findCycle(const std::vector<int>& arr) {
  int p = 0, q = 0;

  while (true) {
    // Check out of bounds.
    if (p < 0 || p >= arr.size() || q < 0 || q >= arr.size()) return false;

    // First step for P.
    p = arr[p];
    if (p == q) return true;
    if (p < 0 || p >= arr.size()) return false;

    // Second step for P.
    p = arr[p];
    if (p == q) return true;

    // First step for Q.
    q = arr[q];
    if (p == q) return true;
  }
}
