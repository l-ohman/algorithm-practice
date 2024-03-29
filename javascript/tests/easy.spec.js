const { expect } = require("chai");
const { BinaryTree, SinglyLinkedList } = require("../utils");
const {
  twoNumberSum,
  isValidSubsequence,
  branchSums,
  closestBstValue,
  removeLinkedListDups,
  GraphNode,
  palindromeCheck,
  minimumWaitTime,
  classPhotos,
  tandemBicycle,
  sortedSquaredArray,
  getNthFib,
  productSum,
  findThreeLargestNumbers,
} = require("../easy");

xdescribe("Two Number Sum", () => {
  it("Returns an array of two numbers when they add up to the target sum", () => {
    const array = [1, 4, -9, 8, 15, 3, -1, 6];
    const targetSum = 10;
    const output = twoNumberSum(array, targetSum);

    expect(output.length).to.equal(2);
    expect(output).to.include(4);
    expect(output).to.include(6);
  });

  it("Return an empty array if no pair adds up to the target sum", () => {
    const array = [10, 14, -7, 4, -1, 7];
    const targetSum = 8;
    expect(twoNumberSum(array, targetSum)).to.eql([]);
  });

  it("Handles input arrays of one number", () => {
    const array = [10];
    const targetSum = 10;
    expect(twoNumberSum(array, targetSum)).to.eql([]);
  });
});

xdescribe("Validate Subsequence", () => {
  it("Returns true when the subsequence is valid", () => {
    let array = [5, 1, 22, 25, 6, -1, 8, 10];
    let sequence = [1, 6, -1, 10];
    expect(isValidSubsequence(array, sequence)).to.equal(true);

    array = [5, 5, 5, 5, 5];
    sequence = [5, 5, 5];
    expect(isValidSubsequence(array, sequence)).to.equal(true);
  });

  it("Returns false when the subsequence is not valid", () => {
    let array = [10, 52, 8, 1, 37, 99, -10];
    let sequence = [52, 8, 99, 1];
    expect(isValidSubsequence(array, sequence)).to.equal(false);

    array = [1, 1, 10, 1];
    sequence = [1, 1, 1, 10];
    expect(isValidSubsequence(array, sequence)).to.equal(false);
  });

  it("Handles subsequences of zero or one integers", () => {
    const array = [10, 52, 8, 1, 37, 99, -10];
    expect(isValidSubsequence(array, [])).to.equal(true);
    expect(isValidSubsequence(array, [1])).to.equal(true);
  });

  it("Handles duplicate numbers in subsequence", () => {
    let array = [1, 4, 7, 9, 15];
    let sequence = [1, 7, 7, 15];
    expect(isValidSubsequence(array, sequence)).to.equal(false);
  });
});

xdescribe("Branch Sums", () => {
  let binaryTree;

  before(() => {
    // constructing a basic BST to test
    const nodes = [];
    for (let i = 0; i < 10; i++) {
      nodes.push(new BinaryTree(i + 1));
    }
    // left side
    nodes[3].left = nodes[7];
    nodes[3].right = nodes[8];
    nodes[4].left = nodes[9];
    nodes[1].left = nodes[3];
    nodes[1].right = nodes[4];
    // right side
    nodes[2].left = nodes[5];
    nodes[2].right = nodes[6];
    // root node
    nodes[0].left = nodes[1];
    nodes[0].right = nodes[2];
    binaryTree = nodes[0];
  });

  it("Output contains the correct number of sums", () => {
    expect(branchSums(binaryTree).length).to.equal(5);
  });

  it("Returns the correct sums", () => {
    expect(branchSums(binaryTree)).to.eql([15, 16, 18, 10, 11]);
  });
});

xdescribe("Find Closest BST Value", () => {
  let binaryTree;
  before(() => {
    let nodes = [10, 5, 15, 2, 5, 13, 22, 1, 14];
    nodes = nodes.map((int) => new BinaryTree(int));

    nodes[3].left = nodes[7];
    nodes[1].left = nodes[3];
    nodes[1].right = nodes[4];
    nodes[2].left = nodes[5];
    nodes[2].right = nodes[6];
    nodes[5].right = nodes[8];

    nodes[0].left = nodes[1];
    nodes[0].right = nodes[2];
    binaryTree = nodes[0];
  });

  it("Returns a single integer", () => {
    expect(closestBstValue(binaryTree, 12)).to.be.a("number");
  });

  it("Returns the closest integer", () => {
    expect(closestBstValue(binaryTree, 12)).to.equal(13);
  });
});

xdescribe("Remove Duplicates From Singly Linked List", () => {
  let linkedListHead;
  before(() => {
    let nodes = [1, 1, 3, 4, 4, 4, 5, 6, 6];
    nodes = nodes.map((int) => new SinglyLinkedList(int));
    for (let i = 0; i < nodes.length - 1; i++) {
      nodes[i].next = nodes[i + 1];
    }
    linkedListHead = removeLinkedListDups(nodes[0]);
  });

  it("The list does not contain duplicates", () => {
    let currentNode = linkedListHead;
    const list = [currentNode];
    while (currentNode.next) {
      list.push(currentNode.next);
      currentNode = currentNode.next;
    }

    for (let i = 0; i < list.length - 1; i++) {
      for (let j = i + 1; j < list.length; j++) {
        // console.log(`Comparing i (${i}: ${list[i].value}) to j (${j}: ${list[j].value})`);
        expect(list[i].value).to.not.equal(list[j].value);
      }
    }
  });

  it("The list maintains its order", () => {
    let currentNode = linkedListHead;

    while (currentNode.next) {
      expect(currentNode.value).to.be.lessThan(currentNode.next.value);
      currentNode = currentNode.next;
    }
  });
});

xdescribe("Graph Depth-First Search", () => {
  let graph;
  before(() => {
    // might try to restructure this into one nested array ...
    const firstNode = new GraphNode("A");
    let children = ["B", "C", "D"];
    children.forEach((itm) => firstNode.addChild(itm));

    children = ["E", "F"];
    children.forEach((itm) => firstNode.children[0].addChild(itm));

    children = ["I", "J"];
    children.forEach((itm) => firstNode.children[0].children[1].addChild(itm));

    children = ["G", "H"];
    children.forEach((itm) => firstNode.children[2].addChild(itm));

    children = ["K"];
    children.forEach((itm) => firstNode.children[2].children[0].addChild(itm));

    graph = firstNode;
  });

  it("Returns an array of the correct size", () => {
    const arr = [];
    graph.depthFirstSearch(arr);
    expect(arr.length).to.equal(11);
  });

  it("Returns the nodes in the correct order", () => {
    const arr = [];
    graph.depthFirstSearch(arr);
    expect(arr).to.eql(["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]);
  });
});

xdescribe("Palindrome Check", () => {
  it("Returns the correct boolean", () => {
    expect(palindromeCheck("racecar")).to.equal(true); // odd
    expect(palindromeCheck("noon")).to.equal(true); // even
    expect(palindromeCheck("cat")).to.equal(false); // odd
    expect(palindromeCheck("palindrome")).to.equal(false); // even
  });

  it("Handles single-character strings", () => {
    expect(palindromeCheck("x")).to.equal(true);
  });
});

xdescribe("Minimum Wait Time", () => {
  it("Returns an integer", () => {
    expect(minimumWaitTime([1, 2, 3])).to.be.a("number");
    expect(minimumWaitTime([5])).to.be.a("number");
  });

  it("Returns the correct value", () => {
    expect(minimumWaitTime([3, 2, 1, 2, 6])).to.equal(17);
    expect(minimumWaitTime([17, 4, 3])).to.equal(10);
  });
});

xdescribe("Class Photos", () => {
  it("Returns a boolean", () => {
    expect(classPhotos([1, 5], [2, 10])).to.be.a("boolean");
  });

  it("Returns the correct value", () => {
    expect(classPhotos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5])).to.equal(true);
  });
});

xdescribe("Tandem Bicycle", () => {
  it("Returns an integer", () => {
    expect(tandemBicycle([1, 2], [3, 4], true)).to.be.a("number");
    expect(tandemBicycle([8], [9], false)).to.be.a("number");
  });

  it("Returns the correct value when 'fastest' is true", () => {
    const redShirts = [5, 5, 3, 9, 2];
    const blueShirts = [3, 6, 7, 2, 1];
    expect(tandemBicycle(redShirts, blueShirts, true)).to.equal(32);
  });

  it("Returns the correct value when 'fastest' is false", () => {
    const redShirts = [5, 5, 3, 9, 2];
    const blueShirts = [3, 6, 7, 2, 1];
    expect(tandemBicycle(redShirts, blueShirts, false)).to.equal(25);
  });
});

xdescribe("Sorted Squared Array", () => {
  it("Returns an array of the correct length", () => {
    expect(Array.isArray(sortedSquaredArray([0]))).to.equal(true);
    expect(Array.isArray(sortedSquaredArray([1, 5, 8, 9]))).to.equal(true);
    expect(sortedSquaredArray([5]).length).to.equal(1);
    expect(sortedSquaredArray([5, 10, 25]).length).to.equal(3);
  });

  it("The output is sorted correctly", () => {
    expect(sortedSquaredArray([2, 7, 8])).to.eql([4, 49, 64]);
    expect(sortedSquaredArray([-5, 0])).to.eql([0, 25]);
    expect(sortedSquaredArray([-8, -3, 2, 5, 9])).to.eql([4, 9, 25, 64, 81]);
    expect(sortedSquaredArray([-5, -4, -3, -2, -1])).to.eql([1, 4, 9, 16, 25]);
  });
});

xdescribe("Get Nth Fibonacci", () => {
  it("Returns an integer", () => {
    expect(getNthFib(1)).to.be.a("number");
    expect(getNthFib(7)).to.be.a("number");
  });

  it("Returns the correct value in the sequence", () => {
    expect(getNthFib(1)).to.equal(0);
    expect(getNthFib(3)).to.equal(1);
    expect(getNthFib(9)).to.equal(21);
  });
});

xdescribe("Product Sum", () => {
  it("Returns an integer", () => {
    expect(productSum([0])).to.be.a("number");
    expect(productSum([4, [2, 3, [1]], 4])).to.be.a("number");
  });

  it("Returns the correct sum", () => {
    expect(productSum([0, [0, [0, 0], 0]])).to.equal(0);
    expect(productSum([1, -3, [-5]])).to.equal(-12);
    expect(productSum([2, [-9, 5, [8, -3]], 4])).to.equal(28);
  });
});

xdescribe("Find Three Largest Numbers", () => {
  let array;
  beforeEach(() => {
    array = [1, 5, 8, 4, 6, 9];
  });

  it("Does not modify the input array", () => {
    const arrayCopy = array.slice();
    findThreeLargestNumbers(array);
    expect(array).to.eql(arrayCopy);
  });

  it("Returns a sorted array of the largest three integers", () => {
    expect(findThreeLargestNumbers(array)).to.eql([6, 8, 9]);
    expect(findThreeLargestNumbers([3, -10, 8, 4])).to.eql([3, 4, 8]);
    expect(findThreeLargestNumbers([1, 1, 1, 1, 1, 1])).to.eql([1, 1, 1]);
  });
});
