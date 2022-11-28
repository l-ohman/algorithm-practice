const { DoublyLinkedListNode: Node } = require("../utils");

// goal: write a class for doubly linked lists. the class should be able to:
// set the head and tail of a linked list.
// insert nodes before and after other nodes as well as at given positions (the first node is '1').
// removing specific nodes, whether by id or by value.
// search for nodes by value.

// assumptions:
// you shouldn't need to create new nodes in these methods.

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  setHead(node) {
    // Write your code here.
  }

  setTail(node) {
    // Write your code here.
  }

  insertBefore(node, nodeToInsert) {
    // Write your code here.
  }

  insertAfter(node, nodeToInsert) {
    // Write your code here.
  }

  insertAtPosition(position, nodeToInsert) {
    // Write your code here.
  }

  removeNodesWithValue(value) {
    // Write your code here.
  }

  remove(node) {
    // Write your code here.
  }

  containsNodeWithValue(value) {
    // Write your code here.
  }
}

module.exports = DoublyLinkedList;
