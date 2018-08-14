
#ifndef _DATA_STRUCTURES_H
#define _DATA_STRUCTURES_H

#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

namespace ds {

/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Node.
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */
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

/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | NodeTree - For Trees/Graphs.
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */
struct NodeTree {
 public:
  int data;
  NodeTree *left, *right;

  NodeTree(int);
  ~NodeTree();
  NodeTree(int, NodeTree*, NodeTree*);
  // Insert operation.
  void insert(int value);
  bool contains(int value);
  void traverse();
  void traverse(const std::string&);
};

struct NodeGraph {
 public:
  int id;
  std::unordered_set<NodeGraph*> adjacent;

  NodeGraph(int);
};

/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | LinkedList.
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */
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

/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Binary Search Tree.
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */
// Tree data Structure.
struct Tree {};

/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Graph data structure.
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */
struct Graph {
 public:
  std::unordered_map<int, NodeGraph*> graphs;

  NodeGraph* getNode(const int&);
  void addEdge(const int&, const int);

  bool hasPathBFS(const int&, const int&);
  bool hasPathDFS(const int&, const int&);

  bool hasPathBFS(const NodeGraph*, const NodeGraph*, std::unordered_set<int>&);
  bool hasPathDFS(const NodeGraph*, const NodeGraph*, std::unordered_set<int>&);
};

// Stack data structure.
struct Stack {};

// Queue data structure.
struct Queue {};

};  // namespace ds

#endif  // _DATA_STRUCTURES_H
