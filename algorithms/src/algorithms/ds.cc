#include "algorithms/ds.hpp"

// #include <functional>
#include <iostream>
#include <utility>

namespace ds {
/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Data Structure: Node
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */

// Node::Node() : data(nullptr), next(nullptr) {
//   std::cout << "Node(" << this->data << ");\n";
// }

Node::Node(int data) : data(data), next(nullptr) {
  // std::cout << "Node(" << this->data << ");\n";
}

Node::Node(int data, Node* next) : data(data), next(next) {}

Node::Node(const Node& node) {
  this->data = node.data;
  this->next = node.next;
}

void Node::print() {
  Node* current = this;

  std::cout << "Node(" << current->data << ")";
  while (current->next != nullptr) {
    std::cout << " -> Node(" << current->next->data << ")";

    current = current->next;
  }

  std::cout << " -> NULL\n";
}

std::ostream& operator<<(std::ostream& stream, const Node& node) {
  stream << "Node(" << node.data << ")";
  // Node* current = (Node*)&node;
  // stream << "Node(" << current->data << ")";
  // while (current->next != nullptr) {
  //   stream << " -> Node(" << current->next->data << ")";

  //   current = current->next;
  // }

  // stream << " -> NULL";
  return stream;
}

/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Data Structure: Binary Node Tree.
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */
NodeTree::NodeTree(int data) : data(data), left(nullptr), right(nullptr) {}
NodeTree::NodeTree(int data, NodeTree* leftNode, NodeTree* rightNode)
    : data(data), left(leftNode), right(rightNode) {}

NodeTree::~NodeTree() {
  delete this->right;
  delete this->left;
}

/** Insert into a binary tree.
 *
 * Complexity:
 *  Best Case:    O(logn)
 *  Average Case: O(logn)
 *  Worst Case:   O(n)
 *
 */
void NodeTree::insert(int value) {
  if (value < this->data) {
    // Insert to the left.
    if (this->left != nullptr)
      this->left = new NodeTree(value);
    else
      this->insert(value);
  } else if (value > this->data) {
    // Insert to the right.
    if (this->right != nullptr)
      this->right = new NodeTree(value);
    else
      this->insert(value);
  } else
    this->data = value;
}

bool NodeTree::contains(int value) {
  // If we're there ,return true.
  if (this->data == value) return true;

  // Traverse and find.
  if (this->data < value) {
    // Ask the left node.
    if (this->left == nullptr) return false;
    return this->contains(value);
  } else {
    // Ask the right node.
    if (this->right == nullptr) return false;
    return this->contains(value);
  }
}

void NodeTree::traverse() { this->traverse("in"); }

void NodeTree::traverse(const std::string& kind) {
  if (kind.compare("in") == 0) {
    // Left -> root -> right.
    if (this->left != nullptr) this->traverse(kind);
    std::cout << this->data << ' ';
    if (this->right != nullptr) this->traverse(kind);
  } else if (kind.compare("pre")) {
    // Root -> left -> right.
    std::cout << this->data << ' ';
    if (this->left != nullptr) this->traverse(kind);
    if (this->right != nullptr) this->traverse(kind);
  } else if (kind.compare("post")) {
    // Left -> right -> root.
    if (this->left != nullptr) this->traverse(kind);
    if (this->right != nullptr) this->traverse(kind);
    std::cout << this->data << ' ';
  } else {
    std::cout << "Values allowed are 'in', 'pre' or 'post'" << '\n';
  }
}

/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Data Structure: LinkedList
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */
LinkedList::LinkedList() : head(nullptr) {}

LinkedList::LinkedList(const Node& head) : head(nullptr) {}

LinkedList::LinkedList(int data) : head(new Node(data)) {}

LinkedList::~LinkedList() { delete this->head; }

/**Traversing a LinkedList
 *
 * Complexity: O(n)
 */
void LinkedList::traverse() {
  this->traverse([](int data) { std::cout << data << ' '; });
}

/**Traversing a LinkedList
 *
 * Complexity: O(n)
 */
void LinkedList::traverse(void (*func)(int)) {
  Node* current = this->head;

  while (current->next != nullptr) {
    // Call a function pointer.
    func(current->data);

    current = current->next;
  }
}

void LinkedList::prepend(int data) {
  Node* newHead = new Node(data);

  // If there exist head, set newHead next element point to current head.
  if (this->head != nullptr) newHead->next = this->head;

  // Prepend newHead to LinkedList.
  this->head = newHead;
}

void LinkedList::append(int data) {
  // If there's no head node.
  if (this->head == nullptr) {
    this->head = new Node(data);
    return;
  }

  // Otherwise we go through till the end.
  Node* current = this->head;
  while (current->next != nullptr) current = current->next;

  // Add element to the end.
  current->next = new Node(data);
}

void LinkedList::insert(int data) { this->insert(data, "post"); }

void LinkedList::insert(int data, const std::string& how) {
  if (how.compare("pre") == 0)
    this->prepend(data);
  else if (how.compare("post") == 0)
    this->append(data);
  else  // Error.
    std::cout << "'pre' or 'post' insertion.\n";
}

Node* LinkedList::remove(int data) {
  if (this->head == nullptr) return nullptr;

  Node* current = this->head;
  while (current->next != nullptr) {
  }

  return nullptr;
}

bool LinkedList::contains(int data) {
  // Head is empty.
  if (this->head == nullptr) return false;

  Node* current = this->head;
  while (current->next != nullptr) {
    if (current->data == data) return true;
    current = current->next;
  }

  return false;
}

/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Data Structures: Graphs.
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */
NodeGraph* Graph::getNode(const int& id) {
  if (this->graphs.find(id) != this->graphs.end()) return this->graphs[id];
  return nullptr;
}

void Graph::addEdge(const int& source, const int dest) {
  NodeGraph* s = this->getNode(source);
  NodeGraph* d = this->getNode(dest);

  s->adjacent.insert(d);
}

int Graph::addNode(const NodeGraph* node) {
  // std::map<int, NodeGraph*>::iterator id = this->graphs.end();
  std::map<int, NodeGraph*>::const_iterator lastNode =
      this->graphs.end();

  std::cout << lastNode->first << " - " << lastNode->second << std::endl;

  return 1;
}

bool Graph::hasPathDFS(const int& source, const int& dest) {
  NodeGraph* s = this->getNode(source);
  NodeGraph* d = this->getNode(dest);
  std::set<int> visited;

  return this->hasPathDFS(s, d, visited);
}

bool Graph::hasPathDFS(const NodeGraph* source, const NodeGraph* dest,
                       std::set<int>& visited) {
  if (visited.find(source->id) != visited.end()) return false;

  visited.insert(source->id);

  if (source == dest) return true;

  for (auto child : source->adjacent)
    if (this->hasPathDFS(child, dest, visited)) return true;

  return false;
}

bool Graph::hasPathBFS(const int& source, const int& dest) {
  NodeGraph* s = this->getNode(source);
  NodeGraph* d = this->getNode(dest);
  std::set<int> visited;

  return this->hasPathBFS(s, d, visited);
}

bool Graph::hasPathBFS(const NodeGraph* source, const NodeGraph* dest,
                       std::set<int>& visited) {
  return false;
}

};  // namespace ds
