const { expect } = require("chai");
const { DoublyLinkedListNode } = require("../utils");
const { taskAssignment, DoublyLinkedList } = require("../medium");

xdescribe("Task Assignment", () => {
  let output;
  beforeEach(() => {
    output = taskAssignment(3, [1, 3, 5, 3, 1, 4]);
    // correctOutput = [[0, 2], [1, 3], [4, 5]];
  });

  it("Returns a nested array", () => {
    expect(output).to.be.an("array");
    expect(taskAssignment(1, [5, 10])).to.be.an("array");
    expect(taskAssignment(1, [5, 10])[0]).to.be.an("array");
  });

  it("Returns the correct assignment of tasks", () => {
    // i do not understand how to effectively check nested arrays with chai ...
    for (let i = 0; i < output.length; i++) {
      if (output[0][0] === 0) {
        expect(output[0][1]).to.equal(2);
      } else if (output[0][0] === 2) {
        expect(output[0][1]).to.equal(0);
      } else if (output[0][0] === 1) {
        expect(output[0][1]).to.equal(3);
      } else if (output[0][0] === 3) {
        expect(output[0][1]).to.equal(1);
      } else if (output[0][0] === 4) {
        expect(output[0][1]).to.equal(5);
      } else if (output[0][0] === 5) {
        expect(output[0][1]).to.equal(4);
      }
    }
  });

  it("The output does not contain any task twice", () => {
    // same as output.flat();
    while (Array.isArray(output[0])) {
      for (let i = 0; i < output[0].length; i++) {
        output.push(output[0][i]);
      }
      output.shift();
    }
    const set = new Set();
    for (let i = 0; i < output.length; i++) {
      set.add(output[i]);
    }

    expect(output.length).to.equal(set.size);
  });
});

// learning experience: it seems like bad practice to have tests depend on eachother
// like this — i cannot run a single test by itself because they share a linked list.
describe("Linked List Construction", () => {
  // example list: [1, 2, 3, 4, 5]
  // standalone nodes on the side: [3, 3, 6]
  let linkedList;
  let node1; // 1
  let node2; // 2
  let node3; // 3
  let node4; // 4
  let node5; // 5

  let node6; // 3
  let node7; // 3
  let node8; // 6

  before(() => {
    node1 = new DoublyLinkedListNode(1);
    node2 = new DoublyLinkedListNode(2);
    node3 = new DoublyLinkedListNode(3);
    node4 = new DoublyLinkedListNode(4);
    node5 = new DoublyLinkedListNode(5);

    node1.next = node2;
    node2.prev = node1;
    node2.next = node3;
    node3.prev = node2;
    node3.next = node4;
    node4.prev = node3;
    node4.next = node5;
    node5.prev = node4;

    linkedList = new DoublyLinkedList();
    linkedList.head = node1;
    linkedList.tail = node5;

    node6 = new DoublyLinkedListNode(3);
    node7 = new DoublyLinkedListNode(3);
    node8 = new DoublyLinkedListNode(6);
  });

  it("setHead", () => {
    expect(linkedList.head).to.equal(node1);
    linkedList.setHead(node4); // [4, 1, 2, 3, 5]
    expect(linkedList.head).to.equal(node4);

    // nodes changed: node4, node1, node3, node5
    expect(node4.prev).to.equal(null);
    expect(node4.next).to.equal(node1);
    expect(node1.prev).to.equal(node4);
    expect(node3.next).to.equal(node5);
    expect(node5.prev).to.equal(node3);
  });

  it("setTail", () => {
    expect(linkedList.tail).to.equal(node5);
    linkedList.setTail(node8); // [4, 1, 2, 3, 5, 6]
    expect(linkedList.tail).to.equal(node8);

    // nodes changed: node8 (6), node5
    expect(node8.prev).to.equal(node5);
    expect(node8.next).to.equal(null);
    expect(node5.next).to.equal(node8);
  });

  it("insertBefore", () => {
    linkedList.insertBefore(node8, node3); // [4, 1, 2, 5, 3, 6]

    // nodes changed: node8 (6), node3, node2, node5
    expect(node8.prev).to.equal(node3);
    expect(node8.next).to.equal(null);
    expect(node3.prev).to.equal(node5);
    expect(node3.next).to.equal(node8);
    expect(node2.next).to.equal(node5);
    expect(node5.prev).to.equal(node2);
    expect(node5.next).to.equal(node3);
  });

  it("insertAfter", () => {
    expect(linkedList.tail).to.equal(node8);
    linkedList.insertAfter(node8, node6); // [4, 1, 2, 5, 3, 6, 3]
    expect(linkedList.tail).to.equal(node6);

    // nodes changed: node8 (6), node6 (3)
    expect(node8.next).to.equal(node6);
    expect(node6.prev).to.equal(node8);
    expect(node6.next).to.equal(null);
  });

  it("insertAtPosition", () => {
    expect(linkedList.head).to.equal(node4);
    linkedList.insertAtPosition(1, node7); // [3, 4, 1, 2, 5, 3, 6, 3]
    expect(linkedList.head).to.equal(node7);

    // nodes changed: node7 (3), node4
    expect(node7.prev).to.equal(null);
    expect(node7.next).to.equal(node4);
    expect(node4.prev).to.equal(node7);
  });

  it("removeNodesWithValue", () => {
    linkedList.removeNodesWithValue(3); // [4, 1, 2, 5, 6]
    expect(linkedList.head).to.equal(node4);
    expect(linkedList.tail).to.equal(node8);

    // nodes changed: node4, node5, node8 (6), all nodes with value 3
    expect(node4.prev).to.equal(null);
    expect(node5.next).to.equal(node8);
    expect(node8.prev).to.equal(node5);
    expect(node8.next).to.equal(null);

    expect(node3.prev).to.equal(null);
    expect(node3.next).to.equal(null);
    expect(node6.prev).to.equal(null);
    expect(node6.next).to.equal(null);
    expect(node7.prev).to.equal(null);
    expect(node7.next).to.equal(null);
  });

  it("remove", () => {
    linkedList.remove(node2); // [4, 1, 5, 6]

    // nodes changed: node4, node1
    expect(node4.next).to.equal(node1);
    expect(node1.prev).to.equal(node4);
  });

  it("containsNodeWithValue", () => {
    expect(linkedList.containsNodeWithValue(2)).to.equal(false);
    expect(linkedList.containsNodeWithValue(5)).to.equal(true);
  });
});
