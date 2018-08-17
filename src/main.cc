#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <iostream>
#include <vector>

#include "../include/Core/Algorithms.h"
#include "../include/Core/DataStructures.h"

int main(int, char**) {
  // Seed random number generator.
  srand(time(0));

  std::vector<int> data;
  data.reserve(10);
  for (int i = 0; i < 10; i++) data.push_back(10 + rand() % 20);  // 10 - 19

  // Custom bubble sort.
  algo::sort::bubble(data);

  // std::sort(data.begin(), data.end());
  int item = 10 + rand() % 20;

  std::cout << "Searching for " << item << " in ";
  std::for_each(data.begin(), data.end(),
                [&](int value) { std::cout << value << ' '; });
  std::cout << '\n';

  // Custom binary search.
  size_t result = algo::search::binarySearch(data, item);

  if (result != algo::npos)
    std::cout << "\nFound at position " << result;
  else
    std::cout << "\nNot found!";

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
