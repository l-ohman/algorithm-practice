// minimum wait time
// difficulty: easy | type: greedy

// input: array of positive integers representing execution time of queries
// the queries will run sequentially; cannot run at the same time
// "wait time" defined as amount of time before a query executes (2nd query is 1st execution time)
// output: minimum possible wait time

function minimumWaitTime(queries) {
  queries.sort((a, b) => a - b); // note: if sort fn not specified, sort treats ints as strings
  let waitTime = 0; // 10
  for (let i = 0; i < queries.length - 1; i++) {
    waitTime += queries[i] * (queries.length - (i + 1));
  }
  return waitTime;
}

module.exports= minimumWaitTime;

// function betterSolution(queries) {
//   queries.sort();
//   let waitTime = 0;
//   let prevWaitTime = 0;

//   for (let i = 0; i < queries.length; i++) {
//     waitTime += prevWaitTime;
//     prevWaitTime += queries[i];
//   }

//   return waitTime;
// }
