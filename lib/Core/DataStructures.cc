#include "../../include/Core/DataStructures.h"
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

Node::Node(const Node& node) { this->data = node.data; }

/*
 * +——————————————————————————————————————————————————————————————————————+
 * | +——————————————————————————————————————————————————————————————————+ |
 * | | Data Structure: LinkedList
 * | +——————————————————————————————————————————————————————————————————+ |
 * +——————————————————————————————————————————————————————————————————————+
 */

LinkedList::LinkedList() : head(nullptr), current(nullptr) {}
LinkedList::LinkedList(Node* head) : head(head), current(nullptr) {}
LinkedList::LinkedList(int data) : head(new Node(data)), current(nullptr) {}

LinkedList::~LinkedList() {
  delete this->head;
  delete this->current;
}

/**Traversing a LinkedList
 *
 * Complexity: O(n)
 */
void LinkedList::traverse() {
  Node* current = this->head;

  while (current->next != nullptr) {
    std::cout << current->data << ' ';
    current = current->next;
  }
}

void LinkedList::append(int data) {
  // If there's no head node.
  if (this->head == nullptr) {
    this->head = new Node(data);
    return;
  }

  // Otherwise we go through till the end.
  this->current = this->head;
  while (this->current->next != nullptr) {
    // std::cout << this->current->data << ' ';
    // Update the next element.
    this->current = this->current->next;
  }

  // Add element to the end.
  this->current->next = new Node(data);
}

void LinkedList::prepend(int data) {}
};  // namespace ds
