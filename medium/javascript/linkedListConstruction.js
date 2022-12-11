const { DoublyLinkedListNode: Node } = require("../../utils");

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
    this.remove(node);
    node.next = this.head;
    this.head && (this.head.prev = node);
    this.head = node;
    if (!this.head.next) {
      this.tail = node;
    }
  }

  setTail(node) {
    this.remove(node);
    node.prev = this.tail;
    this.tail && (this.tail.next = node);
    this.tail = node;
    if (!this.tail.prev) {
      this.head = node;
    }
  }

  insertBefore(node, nodeToInsert) {
    this.remove(nodeToInsert);
    nodeToInsert.prev = node.prev;
    nodeToInsert.next = node;
    node.prev && (node.prev.next = nodeToInsert);
    node.prev = nodeToInsert;

    if (nodeToInsert.prev === null) {
      this.head = nodeToInsert;
    }
  }

  insertAfter(node, nodeToInsert) {
    this.remove(nodeToInsert);
    nodeToInsert.prev = node;
    nodeToInsert.next = node.next;
    node.next && (node.next.prev = nodeToInsert);
    node.next = nodeToInsert;

    if (nodeToInsert.next === null) {
      this.tail = nodeToInsert;
    }
  }

  // note: position of 'head' node is 1
  insertAtPosition(position, nodeToInsert) {
    if (!this.head && position === 1) {
      this.setHead(nodeToInsert);
    } else {
      let selectedNode = this.head;
      while (position > 1) {
        selectedNode = selectedNode.next;
        position -= 1;
      }
      this.insertBefore(selectedNode, nodeToInsert);
    }
  }

  removeNodesWithValue(value) {
    // handles the case of a linked list with 1 item that matches the value
    if (!this.head.next && this.head.value === value) {
      this.remove(this.head);
    }

    let selectedNode = this.head;
    while (selectedNode) {
      const currentNode = selectedNode;
      selectedNode = currentNode.next;
      if (currentNode.value === value) {
        this.remove(currentNode);
      }
    }
  }

  // designing 'remove()' to be used internally like this might be a bad idea...
  // seems that some actions are being repeated multiple times just to reduce # of lines of code.
  // (but i will do it anyway, because i am curious if it can work.)
  remove(node) {
    if (this.tail === node) {
      this.tail = node.prev;
    }
    if (this.head === node) {
      this.head = node.next;
    }

    node.prev && (node.prev.next = node.next);
    node.next && (node.next.prev = node.prev);
    node.prev = null;
    node.next = null;
  }

  containsNodeWithValue(value) {
    let currentNode = this.head;
    while (currentNode) {
      if (currentNode.value === value) {
        return true;
      }
      currentNode = currentNode.next;
    }
    return false;
  }
}

module.exports = DoublyLinkedList;
