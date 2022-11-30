// first time creating / working with heaps.
// note: heap should be represented with an array.

// a binary heap is a 'special' type of binary tree.
// must be COMPLETE, except for last row. when adding, add from left to right.
// heap property: every node is less than the value of its children in a min heap (max heap is opposite).
// heaps are NOT sorted. the most important property is accessing the ROOT node (smallest/largest).

//                8
//           /          \
//        12              23
//     /      \        /     \
//    17      31      30      44
//   /  \    /  \    /  \    /  \
//  22  18

// can be represented as conventional arrays using indicies.
// array of the above heap: [8, 12, 23, 17, 31, 30, 44, 22, 18]
// to get child 1 node => 2i + 1 // 14
// to get child 2 node => 2i + 2
// to get parent node => (i - 1)/2 (rounded down)

class MinHeap {
  constructor(array) {
    this.heap = this.buildHeap(array);
  }

  buildHeap(array=[]) {
    // call sift down on every parent node, starting at the last one (last parent - not last node)
    // to iterate through parents, look at first half of array rounded down(!)
    this.heap = array;
    const parents = array.slice(0, Math.floor(array.length / 2));
    for (let i = parents.length - 1; i >= 0; i--) {
      this.siftDown(i);
    }
    return array; // can also return this.heap, but this works because i have modified the original array
  }

  #swapItems(i, j) {
    const itemI = this.heap[i];
    const itemJ = this.heap[j];
    this.heap[i] = itemJ;
    this.heap[j] = itemI;
  }

  siftDown(i) {
    // compare to the two children nodes, and swap with the smallest (if max heap, use largest)
    if (!this.heap[2 * i + 1] && this.heap[2 * i + 1] !== 0) return;

    let comparisonVal1 = 0;
    if (this.heap[i] > this.heap[2 * i + 1]) {
      comparisonVal1 = Math.abs(this.heap[i] - this.heap[2 * i + 1]);
    }

    let comparisonVal2 = 0;
    if (this.heap[2 * i + 2] || this.heap[2 * i + 2] === 0) {
      if (this.heap[i] > this.heap[2 * i + 2]) {
        comparisonVal2 = Math.abs(this.heap[i] - this.heap[2 * i + 2]);
      }
    }

    if (comparisonVal1 === 0 && comparisonVal2 === 0) {
      return;
    } else if (comparisonVal1 >= comparisonVal2) {
      this.#swapItems(i, 2 * i + 1);
      this.siftDown(2 * i + 1);
    } else if (comparisonVal2 > comparisonVal1) {
      this.#swapItems(i, 2 * i + 2);
      this.siftDown(2 * i + 2);
    }
  }

  siftUp(i) {
    // will continuously swap a number with its parent until it is in the correct place
    if (i === 0) return;

    const parentIndex = Math.floor((i - 1)/ 2);
    if (this.heap[i] < this.heap[parentIndex]) {
      this.#swapItems(i, parentIndex);
      this.siftUp(parentIndex);
    }
  }

  peek() {
    return this.heap[0];
  }

  remove() {
    // removes the min/max value (depending on heap type)
    // swap the ROOT with the final value (0th and (n-1)th items in the array)
    // pop it off the array
    // call siftDown to correctly place the new root
    this.#swapItems(0, this.heap.length - 1);
    const valueRemoved = this.heap.pop();
    this.siftDown(0);
    return valueRemoved;
  }

  insert(value) {
    // gets added to bottom at furthest left (as per heap property)
    // then call siftUp to ensure it is in the right place
    this.heap.push(value);
    this.siftUp(this.heap.length - 1);
  }
}

module.exports = MinHeap;
