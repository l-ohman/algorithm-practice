class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function binaryTreeLogger(root) {
  // TODO - might be useful later
}

class SinglyLinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function linkedListLogger(head) {
  // TODO
}

module.exports = {
  BinaryTree,
  binaryTreeLogger,
  SinglyLinkedList,
  linkedListLogger,
};
