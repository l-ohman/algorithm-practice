// valid starting city (medium)
// set of cities laid out in a circle, connected by clockwise circular road.
// each city has gas station providing some amt of gas, and your car can drive some miles/gallon.
// return the index of the valid starting city.

// assumptions:
// there will always be at least 2 cities.
// it is guaranteed that exactly 1 city will be valid.

// brute force solution - O(n^2)
function validStartingCityBruteForce(distances, fuel, mpg) {
  for (let i = 0; i < distances.length; i++) {
    const attempt = startFromCity(distances, fuel, mpg, i);

    if (attempt === null) continue;
    else return attempt;
  }
  return -1;
}
function startFromCity(distances, fuel, mpg, index = 0) {
  let currentFuel = 0;
  for (let i = 0; i < distances.length; i++) {
    if (i + index >= distances.length) index -= distances.length;

    currentFuel += fuel[i + index] - distances[i + index] / mpg;
    currentFuel = Math.round(currentFuel * 1000) / 1000; // ...

    if (currentFuel < 0) {
      return null;
    }
  }

  if (index < 0) return (index += distances.length);
  else return index;
}

// optimal solution using kadane's algorithm - O(n) time, O(1) space
function validStartingCity(distances, fuel, mpg) {
  let milesRemainingLocal = 0;
  let milesRemainingGlobal = 0;
  let currentBestCity = 0; // index of best candidate

  for (let i = 1; i < distances.length; i++) {
    milesRemainingLocal += fuel[i - 1] * mpg - distances[i - 1];
    // this comparison is made to start at the city directly after the largest fuel deficit
    // (i believe this is only possible because we are guaranteed exactly 1 solution)
    if (milesRemainingLocal < milesRemainingGlobal) {
      milesRemainingGlobal = milesRemainingLocal;
      currentBestCity = i;
    }
  }
  return currentBestCity;
}

// to read more about kadanes algorithim:
// https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

module.exports = validStartingCity;
