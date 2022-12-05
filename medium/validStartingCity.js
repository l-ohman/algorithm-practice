// valid starting city (medium)
// set of cities laid out in a circle, connected by clockwise circular road.
// each city has gas station providing some amt of gas, and your car can drive some miles/gallon.

// inputs:
// array of distances from city i+1 (distance to next city)
// array of gallons of fuel each city provides
// integer representing the car's miles/gallon
// output: the index of the valid starting city

// assumptions:
// there will always be at least 2 cities.
// it is guaranteed that exactly 1 city will be valid.

// this solution is awful (O(n^2)) but it _does_ work...
// apparently there is an O(n) solution using "Kadane's algorithm". (need to research this.)
function validStartingCity(distances, fuel, mpg) {
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
    // ensure we use valid indicies
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

module.exports = validStartingCity;
