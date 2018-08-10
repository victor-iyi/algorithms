
#ifndef _DATA_STRUCTURE_H
#define _DATA_STRUCTURE_H

#include <vector>

namespace ds {

struct Node {
 public:
  int data;
  Node* next;

  Node(int);
  Node(int, Node*);
  Node(const Node&);
  // ~Node();
};

// LinkedList data structure.
struct LinkedList {
 public:
  Node* head;
  Node* current;

  LinkedList();
  LinkedList(int);
  LinkedList(Node*);
  ~LinkedList();

  // Traversal.
  void traverse();

  // Insert
  void append(int);
  void prepend(int);

  // Search
  bool contains(int);

  Node remove(int);
};

// Tree data Structure.
struct Tree {};

// Stack data structure.
struct Stack {};

// Queue data structure.
struct Queue {};
};  // namespace ds

#endif  // _DATA_STRUCTURE_H
