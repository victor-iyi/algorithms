#include <vector>

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

  return false;
}
