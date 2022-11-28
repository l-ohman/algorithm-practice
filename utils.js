class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// function binaryTreeLogger(root) {
//   // TODO - might be useful later
// }

// Node in singly linked list
class SinglyLinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

// Node in doubly linked list
class DoublyLinkedListNode {
  constructor(value) {
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

// function linkedListLogger(head) {
//   // TODO
// }

// function isValidLinkedList(head) {
//   // TODO
// }

module.exports = {
  BinaryTree,
  // binaryTreeLogger,
  SinglyLinkedList,
  DoublyLinkedListNode,
  // linkedListLogger,
};
