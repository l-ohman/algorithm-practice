// medium, greedy
// very similar to 'validStartingCity', but in this iteration there is not a guaranteed single answer - return the lowest valid idx
// pumps as [fuelAmt, distance]

function truckTour(petrolPumps) {
  let validStartIdx = 0;

  let petrol = 0;
  for (let i = 0; i < petrolPumps.length; i++) {
    petrol += petrolPumps[i][0] - petrolPumps[i][1];
    if (petrol < 0) {
      petrol = 0;
      validStartIdx = i + 1;
    }
  }
  return validStartIdx;
}
