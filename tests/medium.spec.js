const { expect } = require("chai");
const { DoublyLinkedListNode } = require("../utils");
const { DoublyLinkedList, taskAssignment } = require("../medium");

// xdescribe("Linked List Construction", () => {
//   let linkedList;
//   before(() => {
//     // example list: [1, 2, 3, 4, 5]
//     // standalone nodes on the side: [3, 3, 6]
//   });

//   it("setHead", () => {
//     // setHead(node 4) => [4, 1, 2, 3, 5]
//   });
//   it("setTail", () => {
//     // setTail(node 6) => [4, 1, 2, 3, 5, 6]
//   });
//   it("insertBefore", () => {
//     // insertBefore(node 6, node 3) => [4, 1, 2, 5, 3, 6]
//   });
//   it("insertAfter", () => {
//     // insertAfter(node 6, other node 3) => [4, 1, 2, 5, 3, 6, 3]
//   });
//   it("insertAtPosition", () => {
//     // insertAtPosition(node 1, node 3) => [3, 4, 1, 2, 5, 3, 6, 3]
//   });
//   it("removeNodesWithValue", () => {
//     // removeNodesWithValue(3) => [4, 1, 2, 5, 6]
//   });
//   it("remove", () => {
//     // remove(node 2) => [4, 1, 5, 6]
//   });
//   it("containsNodeWithValue", () => {
//     // containsNodeWithValue(5) => true
//   });
// });

describe("Task Assignment", () => {
  let output;
  beforeEach(() => {
    output = taskAssignment(3, [1,3,5,3,1,4]);
    // correctOutput = [[0, 2], [1, 3], [4, 5]];
  })

  it("Returns a nested array", () => {
    expect(output).to.be.an("array");
    expect(taskAssignment(1, [5, 10])).to.be.an("array");
    expect(taskAssignment(1, [5, 10])[0]).to.be.an("array");
  });

  it("Returns the correct assignment of tasks", () => {
    // i do not understand how to effectively check nested arrays with chai ...
    for (let i = 0; i < output.length; i++) {
      if (output[0][0]===0) {
        expect(output[0][1]).to.equal(2);
      } else if (output[0][0]===2) {
        expect(output[0][1]).to.equal(0);
      } else if (output[0][0]===1) {
        expect(output[0][1]).to.equal(3);
      } else if (output[0][0]===3) {
        expect(output[0][1]).to.equal(1);
      } else if (output[0][0]===4) {
        expect(output[0][1]).to.equal(5);
      } else if (output[0][0]===5) {
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
    const set = new Set()
    for (let i = 0; i < output.length; i++) {
      set.add(output[i]);
    }

    expect(output.length).to.equal(set.size);
  });
});
