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

function isValidHeap(array, isMinHeap = true) {
  if (!Array.isArray(array)) return false;
  // compare first item to all others in the array
  for (let i = 1; i < array.length; i++) {
    if (isMinHeap && array[0] > array[i]) return false;
    else if (!isMinHeap && array[0] < array[i]) return false;
  }
  // compare each parent to its children // (i - 1) / 2
  for (let i = 1; i < (array.length - 1) / 2; i++) {
    if (isMinHeap) {
      if (array[i] > array[2 * i + 1] || array[i] > array[2 * i + 2]) {
        return false;
      }
    } else {
      // max heap
      if (array[i] < array[2 * i + 1] || array[i] < array[2 * i + 2]) {
        return false;
      }
    }
  }
  return true;
}

module.exports = {
  BinaryTree,
  // binaryTreeLogger,
  SinglyLinkedList,
  DoublyLinkedListNode,
  // linkedListLogger,
  isValidHeap,
};
