// easy, string
// https://www.hackerrank.com/challenges/time-conversion/problem

function timeConversion(s) {
  if (s.slice(0, 2) === "12") {
    if (s[8] === "A") s = "00" + s.slice(2);
  } else if (s[8] === "P") {
    const hour = Number(s.slice(0, 2)) + 12;
    s = hour + s.slice(2);
  }
  return s.slice(0, 8);
}
