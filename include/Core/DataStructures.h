
#ifndef _DATA_STRUCTURES_H
#define _DATA_STRUCTURES_H

#include <string>
#include <vector>

namespace ds {

struct Node {
 public:
  int data;
  Node* next;

  // Node();
  Node(int);
  Node(int, Node*);
  Node(const Node&);
  void print();
  // ~Node();

  friend std::ostream& operator<<(std::ostream&, const Node&);
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
  Node* remove(int);
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

#endif  // _DATA_STRUCTURES_H
