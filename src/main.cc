#include <iostream>
#include <vector>

#include "../include/Core/Algorithms.h"
#include "../include/Core/DataStructures.h"

int main(int, char**) {
  // std::vector<int> values = {0, 1, 2, 3, 4, 5};
  // std::vector<char> values = {'a', 'b', 'c', 'd', 'e', 'f'};
  std::vector<int> values = {'a', 'b', 'c', 'd', 'e', 'f'};

  algo::binarySearch(values, 'a');

  // ds::Node node1(1);
  // ds::Node node2(2);
  // ds::Node node3(3);
  // ds::Node node4(4);
  // ds::Node node5(5);

  // node1.next = &node2;
  // node2.next = &node3;
  // node3.next = &node4;
  // node4.next = &node5;

  // std::cout << "NODES:\n";
  // std::cout << node1 << " > " << node2 << " > " << node3 << " > " << node4
  //           << " > " << node5 << '\n';

  // std::cout << "\nNODE (1): ";
  // node1.print();

  // std::cout << "\nNODE (2): ";
  // node2.print();

  // std::cout << "\nNODE (3): ";
  // node3.print();

  // std::cout << "\nNODE (4): ";
  // node4.print();

  // std::cout << "\nNODE (5): ";
  // node5.print();

  // std::cout << node1 << " => " << node2 << " => " << node3 << " => " << node4
  //           << " => " << node5 << '\n';

  // std::cout << "\n\nLinkedList:\n";

  // ds::LinkedList list1(node1);
  // list1.append(2);
  // list1.traverse();

  return 0;
}
