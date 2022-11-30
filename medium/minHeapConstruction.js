// first time creating / working with heaps.
// note: heap should be represented with an array.

// a binary heap is a 'special' type of binary tree.
// must be COMPLETE, except for last row. when adding, add from left to right.
// heap property: every node is less than the value of its children in a min heap (max heap is opposite).
// heaps are NOT sorted. the most important property is accessing the ROOT node (smallest/largest).
//             8
//         /       \
//       12         23
//     /    \     /    \
//    17    31   30    44
//   /  \
//  22  18
// can be represented as conventional arrays, interestingly enough — using indicies.
// to get child 1 node => 2i + 1 // 14
// to get child 2 node => 2i + 2
// to get parent node => (i - 1)/2 (rounded down)
// array of the above heap: [8, 12, 23, 17, 31, 30, 44, 22, 18]

class MinHeap {
  constructor(array) {
    this.heap = this.buildHeap(array);
  }

  buildHeap(array) {
    // call sift down on every parent node, starting at the last one (last parent - not last node)
    // to iterate through parents, look at first half of array rounded down(!!!)
    // note: sifting up instead is possible, but less efficient
  }

  #siftDown(index) {
    // compare to the two children nodes, and swap with the smallest (if max heap, use largest)
  }

  #siftUp(index) {
    // will continuously swap a number with its parent until it is in the correct place
  }

  peek() {
    // looks at the top value, i'm assuming
  }

  remove() {
    // removes the min/max value (depending on heap type)
    // swap the ROOT with the final value (0th and (n-1)th items in the array)
    // pop it off the array
    // call siftDown to correctly place the new root
  }

  insert(value) {
    // gets added to bottom at furthest left (as per heap property)
    // then call siftUp to ensure it is in the right place
  }
}

module.exports = MinHeap;
