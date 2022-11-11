// input: head of a singly linked list
// output: original linked list, modified to not contain duplicates

// assumptions:
// sorted by value.

function removeLinkedListDups(head) {
  let currentNode = head;

  while(currentNode.next) {
    if (currentNode.next.value === currentNode.value) {
      currentNode.next = currentNode.next.next;
    } else {
      currentNode = currentNode.next;
    }
  }

  return head;
}

module.exports = removeLinkedListDups;
