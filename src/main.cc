#include <iostream>
#include <vector>
#include "../include/Core/DataStructures.h"
#include "Core/Algorithms.h"

int main(int, char**) {
  std::vector<int> values = {0, 1, 2, 3, 4, 5};
  int item = 2;

  ds::Node node1(1);
  ds::Node node2(2);
  ds::Node node3(3);
  ds::Node node4(4);
  ds::Node node5(5);

  node1.next = &node2;
  node2.next = &node3;
  node3.next = &node4;
  node4.next = &node5;

  std::cout << "LinkedList\n" << std::endl;

  ds::LinkedList list1(node1);
  list1.append(2);
  list1.traverse();

  return 0;
}
