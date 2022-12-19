// input: an array of sorted integers
// output: an array of the integers squared, still sorted
// note: numbers in the input array can be negative
// (should attempt to solve without the ".sort" method)

// this method works, but could be simplified with a 'for' loop
// in the correct implementation, there is no 'minAvailable'/'maxAvailable' - only the left/right pointers are necessary

function sortedSquaredArray(array) {
  const output = new Array(array.length).fill(0);
  let leftPointer = 0;
  let rightPointer = array.length - 1;
  let minAvailable = 0;
  let maxAvailable = array.length - 1;

  while (leftPointer <= rightPointer) {
    const minSquared = array[leftPointer] ** 2;
    
    if (array[leftPointer] < 0) {
      const maxSquared = array[rightPointer] ** 2;

      if (minSquared > maxSquared) {
        output[maxAvailable] = minSquared;
        leftPointer++;  
      } else if (maxSquared >= minSquared) {
        output[maxAvailable] = maxSquared;
        rightPointer--;
      }
      maxAvailable--;
    } else {
      output[minAvailable] = minSquared;
      leftPointer++;
      minAvailable++;
    }
  }
  return output;
}

module.exports = sortedSquaredArray;
