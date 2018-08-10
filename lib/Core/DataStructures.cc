#include "../../include/Core/DataStructures.h"

#include <functional>
#include <iostream>

namespace ds {
/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Data Structure: Node
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */

Node::Node(int data) : data(data), next(nullptr) {
  std::cout << "Node(" << this->data << ");\n";
}

Node::Node(int data, Node* next) : data(data), next(next) {}

Node::Node(const Node& node) {
  this->data = node.data;
  this->next = node.next;
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
  while (current->next != nullptr) {
    // std::cout << current->data << ' ';
    // Update the next element.
    current = current->next;
  }

  // Add element to the end.
  current->next = new Node(data);
}

void LinkedList::insert(int data) { this->insert(data, "post"); }

void LinkedList::insert(int data, const std::string& how) {
  if (how.compare("pre") == 0)
    this->prepend(data);
  else if (how.compare("post") == 0)
    this->append(data);
  else
    // Error.
    std::cout << "'pre' or 'post' insertion.\n";
}

Node* LinkedList::remove() { return new Node(1); }
bool LinkedList::contains(int data) { return false; }

};  // namespace ds
