#include <iostream>
#include <vector>
#include "Core/Algorithms.h"

int main(int, char**) {
  std::vector<int> values;
  values.push_back(0);
  values.push_back(1);
  values.push_back(2);
  values.push_back(3);
  values.push_back(4);
  int two = 2;

  algo::binarySearch(values, two);

  return 0;
}
