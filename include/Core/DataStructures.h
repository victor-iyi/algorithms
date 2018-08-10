
#ifndef _DATA_STRUCTURE_H
#define _DATA_STRUCTURE_H

#include <vector>
#include <string>

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

  LinkedList();
  LinkedList(int);
  LinkedList(const Node&);
  ~LinkedList();

  /* Operations */
  // Traversal.
  void traverse();
  void traverse(void (*func)(int));

  // Insert
  void append(int);
  void prepend(int);

  // Search
  bool contains(int);
  Node* remove();
  void insert(int, const std::string&);
  void insert(int);
};

// Tree data Structure.
struct Tree {};

// Stack data structure.
struct Stack {};

// Queue data structure.
struct Queue {};
};  // namespace ds

#endif  // _DATA_STRUCTURE_H
