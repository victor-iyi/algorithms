
#ifndef _DATA_STRUCTURE_H
#define _DATA_STRUCTURE_H

#include <vector>

namespace ds {
// Node data structure.
template <typename T>
class Node {
 public:
  T data;

  Node(T);
  Node(T&);
  ~Node();

};

// LinedList data structure.
class LinedList {};

// Tree data Structure.
class Tree {};

// Stack data structure.
class Stack {};

// Queue data structure.
class Queue {};
};  // namespace ds

#endif  // _DATA_STRUCTURE_H
