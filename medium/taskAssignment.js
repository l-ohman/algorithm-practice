// "task assignment"
// type: greedy

// input: integer (k) representing num of workers, array of durations of tasks
// output: optimal assignment of tasks to workers - an array of arrays containing 2 task indicies each

// assumptions:
// each worker must complete 2 unique tasks (the array comes with 2*k tasks)
// there will always be at least 1 worker
// cannot work on 2 tasks at once
// the workers work in parallel, meaning total time is the max duration for a worker

function taskAssignment(k, tasks) {
  const newTasks = tasks.map((duration, i) => ({i, duration}))
  newTasks.sort((a, b) => a.duration - b.duration);

  let output = [];
  for (let i = 0; i < k; i++) {
    output.push([newTasks.shift().i, newTasks.pop().i]);
  }
  return output;
}

module.exports = taskAssignment;
