
#ifndef _DATA_STRUCTURES_H
#define _DATA_STRUCTURES_H

#include "algorithms_pch.hpp"

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

    // Contains pointer to other nodes connected to this node.
    std::set<NodeGraph*> adjacent;

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
    /*
    graphs = {
      'A': set(['B', 'C']),
      'B': set(['A', 'D', 'F']),
      'C': set(['A', 'D', 'G']),
    }

    graphs = {
      0: [1, 2, 3],
      1: [0, 2, 3],
    }
    */
    std::map<int, NodeGraph*> graphs;

    NodeGraph* getNode(const int&);
    void addEdge(const int&, const int);
    int addNode(const NodeGraph*);

    bool hasPathBFS(const int&, const int&);
    bool hasPathDFS(const int&, const int&);

    bool hasPathBFS(const NodeGraph*, const NodeGraph*, std::set<int>&);
    bool hasPathDFS(const NodeGraph*, const NodeGraph*, std::set<int>&);
  };

  // Stack data structure.
  struct Stack {};

  // Queue data structure.
  struct Queue {};

}  // namespace ds

#endif  // _DATA_STRUCTURES_H