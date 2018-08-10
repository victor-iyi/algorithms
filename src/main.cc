#include <iostream>
#include <vector>
#include "../include/Core/DataStructures.h"
#include "Core/Algorithms.h"

int main(int, char**) {
  std::vector<int> values = {0, 1, 2, 3, 4, 5};
  int item = 2;

  ds::Node node(item);
  ds::LinkedList list1(3);
  ds::LinkedList list2(item);
  list1.prepend(4);
  list1.traverse();

  return 0;
}
