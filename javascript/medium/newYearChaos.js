// medium, array
// https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos/problem

function minimumBribes(q) {
  let bribeCount = 0;
  const expected = [1, 2, 3];

  for (let i = 0; i < q.length; i++) {
    expected.push(expected[2] + 1);
    
    if (q[i] === expected[0]) {
      expected.splice(0, 1);
    } else if (q[i] === expected[1]) {
      bribeCount += 1;
      expected.splice(1, 1);
    } else if (q[i] === expected[2]) {
      bribeCount += 2;
      expected.splice(2, 1);
    } else {
      console.log("Too chaotic");
      return null;
    }
  }
  console.log(bribeCount);
}
